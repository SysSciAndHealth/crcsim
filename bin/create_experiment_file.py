import io
# values for the second chai core run
cost_multipliers = [1/2.5,1/2.25,1/2,1/1.75,1/1.5,1/1.25,2.25,2.5]
effectiveness_increment=[-10,-8,-6,-4,-2,6,8,10]

# values for the third chai core run
#cost_multipliers = [1/2.5,1/2.25,1/2,1/1.75,1/1.5,1/1.25,2.25,2.5]
#effectiveness_increment=[0,2,4]

# values for the fourth chai core run
#cost_multipliers = [1, 1.25, 1.5, 1.75, 2]
#effectiveness_increment=[-10,-8,-6,-4,-2,6,8,10]

count=-1

for j in effectiveness_increment:
    for i in cost_multipliers:
        count = count +1
        with io.open("intervention." + str(count).zfill(4) , 'w', encoding='utf-8') as f:
            f.write("intervene_directMail=true\nparams_QALY_string="+str(i)+","+str(j)+",0,0,0")

for j in effectiveness_increment:
    for i in cost_multipliers:
        count = count +1
        with io.open("intervention." + str(count).zfill(4), 'w', encoding='utf-8') as f:
            f.write("intervene_directMail_patientNavigation=true\nparams_QALY_string="+str(i)+","+str(j)+",0,0,0")

for j in effectiveness_increment:
    for i in cost_multipliers:
        count = count +1
        with io.open("intervention." + str(count).zfill(4), 'w', encoding='utf-8') as f:
            f.write("intervene_patientNavigation=true\nparams_QALY_string="+str(i)+","+str(j)+",0,0,0")
            
for j in effectiveness_increment:
    for i in cost_multipliers:
        count = count +1
        with io.open("intervention." + str(count).zfill(4), 'w', encoding='utf-8') as f:
            f.write("intervene_patientReminder=true\nparams_QALY_string="+str(i)+","+str(j)+",0,0,0")
            
for j in effectiveness_increment:
    for i in cost_multipliers:
        count = count +1
        with io.open("intervention." + str(count).zfill(4), 'w', encoding='utf-8') as f:
            f.write("intervene_academicDetailing=true\nparams_QALY_string="+str(i)+","+str(j)+",0,0,0")
