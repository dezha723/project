def dataset(dirtargets):
    with open(dirtargets) as f1:
        set1 = set(f1.readlines())
    with open("database.txt") as f2:
        set2 = set(f2.readlines())
    nondups = set1 - set2
    print(nondups)
    for i in nondups:
        print(i)
    with open("database.txt", "a") as out:
        out.write("\n")
        out.writelines(nondups)


with open("domain.txt") as tg:
    for target in tg:
     dirtargets="../../../../../../../../../../bug/reconftw/Recon/{targeth}/subdomains/subdomains.txt".format(targeth=target)
     dataset(dirtargets)

