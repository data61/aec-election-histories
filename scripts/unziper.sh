# Thanks - https://stackoverflow.com/a/2463947
for zipfile in *.zip; do
    exdir="${zipfile%.zip}"
    mkdir "$exdir"
    unzip -o -d "$exdir" "$zipfile"
done
