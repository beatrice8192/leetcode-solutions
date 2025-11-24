# https://github.com/noworneverev/leetcode-api
# curl https://leetcode-api-pied.vercel.app/problem/1
# grep python script/0001-1000-python.log | sed 's|python|cpp|g' | xargs -I % sh -c "a=%; dir=\$(dirname \$a); file=\$(basename \$a | cut -c 6-); echo \$dir/\$file; mkdir -p \$dir; echo \"// https://leetcode.com/problems/\$file\" > \$a.cpp; git add \$a.cpp"

start=$1
end=$2
lang_default=python
ext_default=py
[ -z ${start} ] && exit
[ -z ${end} ] && exit
[ ${start} -gt ${end} ] && exit
start_mille=$(( ${start} / 1000 * 1000 ))
dir_default=$(printf "%04d-%04d" $(( ${start_mille} + 1 )) $(( ${start_mille} + 1000 )))

for i in {${start}..${end}}; do
    difficulty=""
    while [[ ${difficulty} == "" ]]; do
        problem=$(curl "https://leetcode-api-pied.vercel.app/problem/${i}" 2>/dev/null | jq "del(.content) | del(.hints) | del(.solution)")
        categoryTitle=$(echo ${problem} | jq -r ".categoryTitle")
        difficulty=$(echo ${problem} | jq -r ".difficulty" | tr '[:upper:]' '[:lower:]')
        isPaidOnly=$(echo ${problem} | jq -r ".isPaidOnly")
        url=$(echo ${problem} | jq -r ".url" | sed "s|/$||g")
        url_file=$(echo ${url} | sed "s|.*/||g")
    done

    if [[ ${categoryTitle} == "Algorithms" ]] || [[ ${categoryTitle} == "Concurrency" ]]; then
        lang=${lang_default}
        ext=${ext_default}
    elif [[ ${categoryTitle} == "Database" ]]; then
        lang=sql
        ext=sql
    elif [[ ${categoryTitle} == "JavaScript" ]]; then
        lang=javascript
        ext=js
    elif [[ ${categoryTitle} == "Shell" ]]; then
        lang=shell
        ext=sh
    else
        lang=$(echo ${categoryTitle} | tr '[:upper:]' '[:lower:]')
        ext=md
    fi
    if [[ ${isPaidOnly} == "true" ]]; then
        isPaidOnly="-locked"
    else
        isPaidOnly=""
    fi
    dir=$(printf "${dir_default}${isPaidOnly}-${difficulty}-${lang}")
    file=$(printf "%04d-%s\n" ${i} ${url_file})
    echo ${dir}/${file}

    if ! [ -e ${dir}/${file}.${ext} ] && ! [ -e ${dir}/${file}-v1.${ext} ]; then
        mkdir -p ${dir}
        echo "# ${url}" > ${dir}/${file}.${ext}
        git add ${dir}/${file}.${ext}
    fi
done
