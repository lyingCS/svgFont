import fontforge
F = fontforge.open('fz.TTF')
for name in F:
    filename = "./svg/"+str(F[name].unicode) +'_'+name+ '.svg'
    F[name].export(filename)
