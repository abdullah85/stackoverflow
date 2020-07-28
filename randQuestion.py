#https://stackoverflow.com/questions/9755538/how-do-i-create-a-list-of-random-numbers-without-duplicates/9755612#9755612
import random, math

def extractSamplesQuick(populationSize, sampleSize, interval, leafSize = 1) :
    (start, end) = interval
    if ((end - start) < (sampleSize - 1)): # Ideally, should not be reachable for our usage
        raise ValueError("interval ("+str(start) +","+ str(end)+") smaller than "+ str(sampleSize))
    if(sampleSize <= leafSize) :
        return extractSamples(populationSize, sampleSize, [interval] )
    len1, len2 = int(math.floor(sampleSize/2.0)), int(math.ceil(sampleSize/2.0))
    # we have (len1 + len2) = sampleSize
    offset   = random.randint( (start + len1 - 1), (end - len2) )
    # indices carefully chosen above to tally with statement below...
    iL1, iL2 = (start, offset), (offset+1, end)
    samples1 = extractSamplesQuick(populationSize, len1, iL1, leafSize)
    samples2 = extractSamplesQuick(populationSize, len2, iL2, leafSize)
    samples  = []
    i1 = i2 = 0
    while(i1 < len1 and i2 < len2) :
        chosenLst = random.choice([0,1])
        if (chosenLst == 0) :
            samples.append(samples1[i1])
            i1 += 1
        else :
            samples.append(samples2[i2])
            i2 += 1
    if (i1 < len1) :
        samples += samples1[i1:]
    else :
        samples += samples2[i2:]
    return samples

def extractSamples(populationSize, sampleSize, intervalLst) :
    if (sampleSize > populationSize) :
        raise ValueError("sampleSize = "+str(sampleSize) +", is less than populationSize (= " + str(populationSize) + ")")
    samples = []
    while (len(samples) < sampleSize) :
        i = random.randint(0, (len(intervalLst)-1))
        (a,b) = intervalLst[i]
        sample = random.randint(a,b)
        if (a==b) :
            intervalLst.pop(i)
        elif (a == sample) : # shorten beginning of interval
            intervalLst[i] = (sample+1, b)
        elif ( sample == b) : # shorten interval end
            intervalLst[i] = (a, sample - 1)
        else :
            intervalLst[i] = (a, sample - 1)
            intervalLst.append((sample+1, b))
        samples.append(sample)
    return samples

def aakExtractSamplesQuick(populationSize, sampleSize, leafSize=1):
    import pdb; pdb.set_trace();
    return extractSamplesQuick(populationSize, sampleSize, (0,populationSize-1), leafSize)

def aakExtractSamples(populationSize, sampleSize):
    return extractSamples(populationSize, sampleSize, [(0,populationSize-1)])

# https://stackoverflow.com/a/9755612/10645311 (Greg Hewgill)
def pyRandSample(populationSize, sampleSize):
    return random.sample(range(populationSize), sampleSize)
def extractSamplesInbuilt(populationSize, sampleSize):
    return random.sample(range(populationSize), sampleSize)

# https://stackoverflow.com/a/38398873/10645311
# Is it incorrect? (as it solves by generating samples when sampleSize > populationSize)
# Uses yield, does solve for large values
def random_sample(count, start, stop, step=1):
    def gen_random():
        while True:
            yield random.randrange(start, stop, step)

    def gen_n_unique(source, n):
        seen = set()
        seenadd = seen.add
        for i in (i for i in source() if i not in seen and not seenadd(i)):
            yield i
            if len(seen) == n:
                break

    return [i for i in gen_n_unique(gen_random,
                                    min(count, int(abs(stop - start) / abs(step))))]

# https://stackoverflow.com/a/9755612/10645311
def setApproach(populationSize, sampleSize):
    answer = set()
    answerSize = 0

    while answerSize < sampleSize:
        r = random.randint(0,100)
        if r not in answer:
            answerSize += 1
            answer.add(r)

    return answerSize

# https://stackoverflow.com/a/45500580/10645311
def numPySolution(populationSize, sampleSize):
    import numpy as np
    a = np.linspace( 0, populationSize - 1, sampleSize )
    random.shuffle(a)
    print(a)
