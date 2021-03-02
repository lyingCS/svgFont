import pickle

with open('dalpha200.dat', 'rb') as f:
    dalpha200=pickle.load(f)

limit=130
dalpha={k:(limit if v>limit else v) for (k,v) in dalpha200.items()}

OPfilename='dalpha'+str(limit)+'.dat'
dalpha['svg/22281_uni5709_1000.svg']=200
dalpha['svg/22282_uni570A_1000.svg']=200
dalpha['svg/33564_uni831C_1000.svg']=200
dalpha['svg/33740_uni83CC_1000.svg']=200
dalpha['svg/37003_uni908B_1000.svg']=200
dalpha['svg/37193_uni9149_1000.svg']=200
dalpha['svg/58214_uniE366_1000.svg']=200

with open(OPfilename,'wb') as f:
	pickle.dump(dalpha,f)

print(dalpha)