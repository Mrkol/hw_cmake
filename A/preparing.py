

source = ["#pragma once",
        "",
        "//jaja, naturlich, das ist index.h"
        ""]

print("SCRIPT FIRED")

with open("./index.h", 'w') as file:
    for line in source:
        file.write(line + "\n");

