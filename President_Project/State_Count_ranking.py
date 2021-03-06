import SentimentAnalysis as SA
def state_count(name):
    searchfile = open(name + "_SortedFiltered.json", "r")
    line = searchfile.readline()    
    state_count = 0
    states = {'AL':0, 'AK':0, 'AZ':0, 'AR':0, 'CA':0, 'CO':0, 'CT':0, 'DE':0, 'FL':0,
              'GA':0, 'HI':0, 'ID':0, 'IL':0, 'IN':0, 'IA':0, 'KS':0, 'KY':0, 'LA':0,
              'ME':0, 'MD':0, 'MA':0, 'MI':0, 'MN':0, 'MS':0, 'MO':0, 'MT':0, 'NE':0,
              'NV':0, 'NH':0, 'NJ':0, 'NM':0, 'NY':0, 'NC':0, 'ND':0, 'OH':0, 'OK':0,
              'OR':0, 'PA':0, 'RI':0, 'SC':0, 'SD':0, 'TN':0, 'TX':0, 'UT':0, 'VT':0,
              'VA':0, 'WA':0, 'WV':0, 'WI':0, 'WY':0}

    textAI = SA.analyzer()
    while line:
        a = line.lower()
        if " al\"" in a or "alabama" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['AL'] += 1
        if " ak\"" in a or "alaska" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['AK'] += 1
        if " az\"" in a or "arizona" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['AZ'] += 1
        if " ar\"" in a or "arkansas" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['AR'] += 1
        if " ca\"" in a or "california" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['CA'] += 1
        if " co\"" in a or "colorado" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['CO'] += 1
        if " ct\"" in a or "connecticut" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['CT'] += 1
        if " de\"" in a or "delaware" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['DE'] += 1
        if " fl\"" in a or "florida" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['FL'] += 1
        if " ga\"" in a or "georgia" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['GA'] += 1
        if " hi\"" in a or "hawaii" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['HI'] += 1
        if " id\"" in a or "idaho" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['ID'] += 1
        if " il\"" in a or "illinois" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['IL'] += 1
        if " in\"" in a or "indiana" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['IN'] += 1
        if " ia\"" in a or "iowa" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['IA'] += 1
        if " ks\"" in a or "kansas" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['KS'] += 1
        if " ky\"" in a or "kentucky" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['KY'] += 1
        if " la\"" in a or "louisiana" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['LA'] += 1
        if " me\"" in a or "maine" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['ME'] += 1
        if " md\"" in a or "maryland" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['MD'] += 1
        if " ma\"" in a or "massachusetts" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['MA'] += 1
        if " mi\"" in a or "michigan" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['MI'] += 1
        if " mn\"" in a or "minnesota" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['MN'] += 1
        if " ms\"" in a or "mississippi" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['MS'] += 1
        if " mo\"" in a or "missouri" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['MO'] += 1
        if " mt\"" in a or "montana" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['MT'] += 1
        if " ne\"" in a or "nebraska" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['NE'] += 1
        if " nv\"" in a or "nevada" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['NV'] += 1
        if " nh\"" in a or "new hampshire" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['NH'] += 1
        if " nj\"" in a or "new jersey" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['NJ'] += 1
        if " nm\"" in a or "new mexico" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['NM'] += 1
        if " ny\"" in a or "new york" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['NY'] += 1
        if " nc\"" in a or "north carolina" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['NC'] += 1
        if " nd\"" in a or "north dakota" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['ND'] += 1
        if " oh\"" in a or "ohio" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['OH'] += 1
        if " ok\"" in a or "oklahoma" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['OK'] += 1
        if " or\"" in a or "oregon" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['OR'] += 1
        if " pa\"" in a or "pennsylvania" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['PA'] += 1
        if " ri\"" in a or "rhode island" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['RI'] += 1
        if " sc\"" in a or "south carolina" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['SC'] += 1
        if " sd\"" in a or "south dakota" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['SD'] += 1
        if " tn\"" in a or "tennessee" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['TN'] += 1
        if " tx\"" in a or "texas" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['TX'] += 1
        if " ut\"" in a or "utah" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['UT'] += 1
        if " vt\"" in a or "vermont" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['VT'] += 1
        if " va\"" in a or "virginia" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['VA'] += 1
        if " wa\"" in a or "washington" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['WA'] += 1
        if " wv\"" in a or "west virginia" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['WV'] += 1
        if " wi\"" in a or "wisconsin" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['WI'] += 1
        if " wy\"" in a or "wyoming" in a:
            line = searchfile.readline()
            if (textAI.getSingleSentiment2(line) == 'pos'):
                states['WY'] += 1
        else:
            line = searchfile.readline()
        line = searchfile.readline()
    searchfile.close()
    return states

def state_winner(dictionary_presidents):
    import operator
    states = {'AL':{}, 'AK':{}, 'AZ':{}, 'AR':{}, 'CA':{}, 'CO':{}, 'CT':{}, 'DE':{}, 'FL':0,
              'GA':{}, 'HI':{}, 'ID':{}, 'IL':{}, 'IN':{}, 'IA':{}, 'KS':{}, 'KY':{}, 'LA':0,
              'ME':{}, 'MD':{}, 'MA':{}, 'MI':{}, 'MN':{}, 'MS':{}, 'MO':{}, 'MT':{}, 'NE':0,
              'NV':{}, 'NH':{}, 'NJ':{}, 'NM':{}, 'NY':{}, 'NC':{}, 'ND':{}, 'OH':{}, 'OK':0,
              'OR':{}, 'PA':{}, 'RI':{}, 'SC':{}, 'SD':{}, 'TN':{}, 'TX':{}, 'UT':{}, 'VT':0,
              'VA':{}, 'WA':{}, 'WV':{}, 'WI':{}, 'WY':{}}
    candidates = ['Trump', "Clinton", "Bernie", "Cruz", "Kasich"]
    new_dict = states
    states = states.keys()
    for statename in sorted(states):
        new_dict[statename] = {}
    for statename in sorted(states):
        for pres in candidates:
            new_dict[statename][pres] = dictionary_presidents[pres][statename]
    for statename in sorted(states):
        new_dict[statename] = sorted(new_dict[statename].items(), key=operator.itemgetter(1))
        new_dict[statename].reverse()
        print statename, new_dict[statename][0:5]
        writefile.write(statename)
        writefile.write(str(new_dict[statename]))
        writefile.write("\n")
      


#set inital counts to 0
states = {'AL':0, 'AK':0, 'AZ':0, 'AR':0, 'CA':0, 'CO':0, 'CT':0, 'DE':0, 'FL':0,
          'GA':0, 'HI':0, 'ID':0, 'IL':0, 'IN':0, 'IA':0, 'KS':0, 'KY':0, 'LA':0,
          'ME':0, 'MD':0, 'MA':0, 'MI':0, 'MN':0, 'MS':0, 'MO':0, 'MT':0, 'NE':0,
          'NV':0, 'NH':0, 'NJ':0, 'NM':0, 'NY':0, 'NC':0, 'ND':0, 'OH':0, 'OK':0,
          'OR':0, 'PA':0, 'RI':0, 'SC':0, 'SD':0, 'TN':0, 'TX':0, 'UT':0, 'VT':0,
          'VA':0, 'WA':0, 'WV':0, 'WI':0, 'WY':0}

candidates = ['Trump', "Clinton", "Bernie", "Cruz", "Kasich"]
writefile = open("State_Count_slow.json", "w")
dictionary_inception = {}
for name in candidates:
    states = state_count(name)
    #print state_count(name)
    writefile.write(name)
    writefile.write("\n")
    dictionary_inception[name] = states
    print name
    for statename in sorted(states):
        writefile.write(statename)
        writefile.write(' ')
        writefile.write(str(states[statename]))
        writefile.write("\n")
        print statename, states[statename]
    print
    print
    writefile.write("\n")
    writefile.write("\n")
#state_winner(dictionary_inception)
writefile.close()





        
