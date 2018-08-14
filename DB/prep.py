import sqlite3
import pandas as pd

data = pd.read_csv('ODG_Sample.csv', index_col = None)
sheet = data
sqlite_db = sqlite3.connect('ODG.sqlite3')#need to be changed!
cursor = sqlite_db.cursor()
claim_problem = []
claim_noothertrt = []
for index in range(len(sheet.index)):
    row = sheet.iloc[index, :]
    claim_no = int(row['1_Claim-No'])# key for all the tables
    ICD9_code = row['6_ICD9-Code_MV'].split('^')
    ICD9_date = row['7_ICD9-Date_MV'].split('^')
    if len(ICD9_code) != len(ICD9_date):
        claim_problem.append(claim_no)
        continue
    ICD9s = zip(ICD9_code, ICD9_date)
     # ICD9 table
    pcode = str(row['14_Procedure-Code_MV']).split('^')
    p_date = str(row['15_Date-of-Service_MV']).split('^')
    p_amount_paid = [float(p) for p in str(row['16_Amount-Paid_MV']).split('^') if p!='']
    p_num = [int(p) for p in str(row['17_Number-of-Units_MV']).split('^') if p!='']
    ICD9_PC = str(row['18_ICD9-for-PC_MV']).split('^')
    if (len(pcode) != len(p_date) or\
        len(pcode) != len(p_amount_paid) or\
        len(pcode) != len(p_num) or\
        len(pcode) != len(ICD9_PC)):
        claim_problem.append(claim_no)
        continue
    procedures = zip(pcode, p_date, p_amount_paid, p_num, ICD9_PC)
     #Procedure code table
    try:
        OT = row['19_Other-Treatment-Code_MV'].split('^')
        o_date = str(row['20_Date-of-Service_MV']).split('^')
        o_amount_paid = [float(p) for p in str(row['21_Amount-Paid_MV']).split('^') if p!='']
        o_num = [int(p) for p in str(row['22_Number-of-Units_MV']).split('^') if p!='']
        if (len(OT) != len(o_date) or\
            len(OT) != len(o_amount_paid) or\
            len(OT) != len(o_num)):
            claim_problem.append(claim_no)
            continue
            #Other treatment table
        others = zip(OT, o_date, o_amount_paid, o_num)
    except ValueError:
        claim_noothertrt.append(claim_no)
    date_injury = str(row['2_Date-of-Injury'])
    age = int(row['3_Age'])
    gender = row['4_Gender']
    NCCI = int(row['5_NCCI-Code'])
    legal = row['8_Legal-Representation']
    last_work = row['9_Last-Day-Worked_MV']#need to be changed
    if last_work == 'NaN':
        claim_problem.append(claim_no)
        continue
    try:
        absence = int(row['10_Days-This-Absence_MV'])
    except ValueError:
        claim_problem.append(claim_no)
        continue
    total_duration = int(row['12_Total-Disability-Duration'])
    indemnity_cost = float(row['13_Total-Indemnity-Costs'])
    med_cost = float(row['23_Total-Medical-Costs'])
    total_cost = float(row['24_Total-Costs'])
    cursor.execute(
        "INSERT INTO patients(claim_no, date_injury, age, gender, NCCI, \
        legal, last_work, absence, total_duration, indemnity_cost, med_cost, total_cost)\
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ",
        (claim_no, date_injury, age, gender, NCCI, legal, last_work, \
        absence, total_duration, indemnity_cost, med_cost, total_cost)
    )
    for ICD9 in ICD9s:
        cursor.execute(
            "INSERT INTO icd9(claim_no, code, date_code) VALUES(?, ?, ?)", \
            (claim_no, ICD9[0], ICD9[1])
        )
    for procedure in procedures:
        cursor.execute(
            "INSERT INTO pc(claim_no, pcode, date_service, amount_paid, number_unit, ICD9_PC)\
             VALUES(?, ?, ?, ?, ?, ?)", \
             (claim_no, procedure[0], procedure[1], procedure[2], procedure[3], procedure[4])
        )
    for other in others:
        cursor.execute(
            "INSERT INTO ot(claim_no, OT, date_service, amount_paid, number_unit)\
            VALUES (?, ?, ?, ?, ?)", \
            (claim_no, other[0], other[1], other[2], other[3])
        )
problem = [str(num) for num in claim_problem]
with open('claim_problem.txt','w') as f1:
    f1.write('\n'.join(problem))
notrt = [str(num) for num in claim_noothertrt]
with open('claim_noothertrt.txt','w') as f2:
    f2.write('\n'.join(claim_noothertrt))
sqlite_db.commit()
sqlite_db.close()
