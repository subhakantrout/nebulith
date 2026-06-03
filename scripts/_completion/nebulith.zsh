#compdef nebulith nebulith-backup nebulith-calendar nebulith-contacts nebulith-cookbook nebulith-docs nebulith-gallery nebulith-mail nebulith-mcp nebulith-memory nebulith-notes nebulith-personal nebulith-preset nebulith-research nebulith-sessions nebulith-signature nebulith-skills nebulith-tasks nebulith-theme nebulith-webhook
# Zsh tab-completion for the nebulith umbrella + sub-CLIs.
#
# Drop in any directory on $fpath, e.g.:
#     fpath=(/path/to/nebulith-ui/scripts/_completion $fpath)
#     autoload -U compinit; compinit
#
# Then `nebulith <tab>` completes subcommands; `nebulith mail <tab>`
# completes mail subcommands; `nebulith-mail <tab>` works the same.

_nebulith_scripts_dir() {
    local self="${(%):-%x}"
    while [[ -L "$self" ]]; do self="$(readlink "$self")"; done
    cd "${self:h}/.." && pwd
}

typeset -gA _nebulith_subs

_nebulith_refresh() {
    _nebulith_subs=()
    local dir="$(_nebulith_scripts_dir)"
    local py="$dir/../venv/bin/python"
    [[ -x "$py" ]] || py="$(command -v python3)"
    local f sub help_out commands
    for f in "$dir"/nebulith-*; do
        [[ -x "$f" ]] || continue
        case "$f" in
            *.bak|*.pyc|*.pre-*) continue ;;
        esac
        sub="${${f:t}#nebulith-}"
        help_out=$("$py" "$f" --help 2>/dev/null) || continue
        commands=$(echo "$help_out" | grep -oE '\{[a-z0-9_,-]+\}' | head -1 \
            | tr -d '{}' | tr ',' ' ')
        _nebulith_subs[$sub]="$commands"
    done
}

_nebulith() {
    [[ ${#_nebulith_subs} -eq 0 ]] && _nebulith_refresh

    local cmd="${words[1]}"

    if [[ "$cmd" == "nebulith" ]]; then
        if (( CURRENT == 2 )); then
            local -a subs=(${(k)_nebulith_subs} help)
            _describe 'subcommand' subs
            return
        fi
        local sub="${words[2]}"
        if [[ "$sub" == "help" ]] && (( CURRENT == 3 )); then
            local -a subs=(${(k)_nebulith_subs})
            _describe 'subcommand' subs
            return
        fi
        if (( CURRENT == 3 )); then
            local -a sc=(${(s/ /)_nebulith_subs[$sub]})
            _describe 'command' sc
            return
        fi
        return
    fi

    # nebulith-foo <tab>
    local sub="${cmd#nebulith-}"
    if (( CURRENT == 2 )); then
        local -a sc=(${(s/ /)_nebulith_subs[$sub]})
        _describe 'command' sc
        return
    fi
}

_nebulith "$@"
