def hashkeygenerator(array):
    hashkey = {}
    result = []
    highestcompletedid = 0
    for i in range(len(array)):
        splited = array[i].split(";")
        name = splited[0]
        if len(splited) < 3:
            startorid = splited[1]
            if name in hashkey:
                if startorid == "START":
                    hashkey[name] = {"mostRecentCompletion": highestcompletedid, "line": i}
                else:
                    if int(startorid) < hashkey[name]["mostRecentCompletion"]:
                        result.append([hashkey[name]['Line'], name, "SHORTENED_JOB"])
                    elif highestcompletedid < int(startorid):
                        highestcompletedid = int(startorid)
            else:
                hashkey[name] = {"mostRecentCompletion": highestcompletedid, "line": i}

        else:
            startorid = splited[1:]
            if name in hashkey:
                for id in range(len(startorid)):
                    startorid[id] = int(startorid[id])

                if min(startorid) < highestcompletedid:
                    string = str(i) + ";" + name + ";" + "SUSPICIOUS_BATCH"
                    result.append(string)

                elif max(startorid) > highestcompletedid:
                    highestcompletedid = max(startorid)

    return result

