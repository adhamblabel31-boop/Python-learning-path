# ----------------------------------------------------
#! ------- function parameters and arguments ---------
# ----------------------------------------------------
# f,m,l="Adham","Yasser","Abo Blabel"
# print(f"{f} {m} {l}")


def name(f, m, l):
    print(f"{f} {m} {l}")


name("Adham", "Yasser", "Abo Blabel")


def sum(f, s):
    if type(f) != int or type(s) != int:
        print("integer only")
    else:
        print(f + s)


sum(2, 4)


def fullName(f, m, l):
    print(f"Hi , {f.strip().capitalize()} {m.strip().capitalize():.1s} {l.strip()}")


fullName("         Adham        ", " yasser", "Abo Blabel           ")
