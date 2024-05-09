responses = {
    'q1': 'Always', 'q2': 'Sometimes', 'q3': 'Often', 'q4': 'Rarely', 'q5': 'Sometimes',
    'q6': 'Sometimes', 'q7': 'Rarely', 'q8': 'Rarely', 'q9': 'Often', 'q10': 'Rarely',
    'q11': 'Rarely', 'q12': 'Rarely', 'q13': 'Never', 'q14': 'Sometimes', 'q15': 'Sometimes',
    'q16': 'Rarely', 'q17': 'Sometimes', 'q18': 'Sometimes', 'q19': 'Rarely', 'q20': 'Rarely',
    'q21': 'Never', 'q22': 'Never', 'q23': 'Rarely', 'q24': 'Often', 'q25': 'Sometimes',
    'q26': 'Rarely', 'q27': 'Sometimes', 'q28': 'Sometimes', 'q29': 'Never', 'q30': 'Never',
    'q31': 'Sometimes', 'q32': 'Sometimes', 'q33': 'Always', 'q34': 'Rarely', 'q35': 'Always',
    'q36': 'Rarely', 'q37': 'Never', 'q38': 'Sometimes', 'q39': 'Often', 'q40': 'Rarely',
    'q41': 'Rarely', 'q42': 'Sometimes', 'q43': 'Always', 'q44': 'Rarely', 'q45': 'Sometimes',
    'q46': 'Never', 'q47': 'Always', 'q48': 'Sometimes', 'q49': 'Always', 'q50': 'Never'
}

# Convert dictionary values to a list
type = [
    'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 
    'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 
    'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 
    'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 
    'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B'
]

def a(x):
    if x=="Always":
        return 1
    elif x=="Often":
        return 2
    elif x=="Sometimes":
        return 3
    elif x=="Rarely":
        return 4
    elif x=="Never":
        return 5
    

def b(x):
    if x=="Always":
        return 5
    elif x=="Often":
        return 4
    elif x=="Sometimes":
        return 3
    elif x=="Rarely":
        return 2
    elif x=="Never":
        return 1


def slv(responses):
    responses = list(responses.values())
    # print(a(responses[0])+1)
    Leadership_Understanding_A = a(responses[0])+a(responses[10])+a(responses[40])

    Leadership_Understanding_B= b(responses[20])

    # # Strategic_Orientation_A= 
    Strategic_Orientation_B= b(responses[1]) + b(responses[8]) + b(responses[19]) + b(responses[24]) + b(responses[47])

    # # Mentoring_A=
    Mentoring_B= b(responses[2]) + b(responses[16]) + b(responses[28]) + b(responses[38]) + b(responses[43])

    Authenticity_A=a(responses[3]) + a(responses[14]) +a(responses[44])
    Authenticity_B=b(responses[26]) + b(responses[31] )

    Interpersonal_Skills_A=a(responses[12])+ a(responses[34])
    Interpersonal_Skills_B=b(responses[4]) + b(responses[25]) + b(responses[42])

    Decisiveness_A=a(responses[5])+ a(responses[39])
    Decisiveness_B=b(responses[13]) + b(responses[32]) + b(responses[48])

    Teamwork_A=a(responses[6]) + a(responses[21]) + a(responses[36])
    Teamwork_B=b(responses[17]) + b(responses[29])

    Time_Priority_A=a(responses[7]) + a(responses[15]) + a(responses[27]) + a(responses[37])
    Time_Priority_B=b(responses[46])

    Result_Orientation_A=a(responses[22]) + a(responses[23] )
    Result_Orientation_B=b(responses[11]) + b(responses[33]) + b(responses[35])

    Leadership_Personality_A=a(responses[18])+ a(responses[30]) + a(responses[41]) 
    Leadership_Personality_B=b(responses[9]) + b(responses[45])

    Leadership_Understanding = Leadership_Understanding_A + Leadership_Understanding_B
    Strategic_Orientation = Strategic_Orientation_B
    Mentoring = Mentoring_B
    Authenticity = Authenticity_A + Authenticity_B
    Interpersonal_Skills = Interpersonal_Skills_A+Interpersonal_Skills_B
    Decisiveness = Decisiveness_A + Decisiveness_B
    Teamwork = Teamwork_A + Teamwork_B
    Time_Priority = Time_Priority_A + Time_Priority_B
    Result_Orientation = Result_Orientation_A + Result_Orientation_B
    Leadership_Personality = Leadership_Personality_A + Leadership_Personality_B
    
    res1 = [Leadership_Understanding,
    Strategic_Orientation ,
    Mentoring ,
    Authenticity,
    Interpersonal_Skills ,
    Decisiveness,
    Teamwork ,
    Time_Priority ,
    Result_Orientation ,
    Leadership_Personality]
    
    ele_list = ["Leadership_Understanding",
    "Strategic_Orientation" ,
   "Mentoring" ,
   "Authenticity",
   "Interpersonal_Skills" ,
    "Decisiveness",
    "Teamwork" ,
    "Time_Priority" ,
    "Result_Orientation" ,
    "Leadership_Personality"]
    res = max(res1)

    print(ele_list[res1.index(res)])
    return ele_list[res1.index(res)]
slv(responses)