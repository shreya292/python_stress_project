#compdef nginx-prometheus-exporter

_nginx-prometheus-exporter() {
    local matches=($(${words[1]} --completion-bash "${(@)words[2,$CURRENT]}"))
    compadd -a matches

    if [[ $compstate[nmatches] -eq 0 && $words[$CURRENT] != -* ]]; then
        _files
    fi
}

if [[ "$(basename -- ${(%):-%x})" != "_nginx-prometheus-exporter" ]]; then
    compdef _nginx-prometheus-exporter nginx-prometheus-exporter
fi
