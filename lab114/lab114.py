import matplotlib.pyplot as plt


def factorial(n):
    s = 1
    for i in range(2, n+1):
        s = s*i
    return s


file = "exp.txt"
kas = [10]

f = open(file, 'r')
s = f.readline()
data = []
for i in range(4000):
    s = f.readline()
    data.append(int(s))

for k in kas:
    a = []
    count = {}
    count['k'] = k
    med = 0
    for i in range(4000//k):
        s = 0
        for j in range(k):
            s += data[k*i+j]
        a.append(s)
        med += s
    med = med/len(a)
    count['med'] = med
    sko = 0
    for i in a:
        sko = sko + (i - med)**2
    sko = (sko/len(a))**0.5
    count['sko'] = sko
    count['sqrtmed'] = med**0.5
    count['sterror'] = sko/(len(a))**0.5
    count['otnrass'] = sko/med * 100
    count['otnerror1'] = count['sterror']/med*100
    count['otnerror2'] = 100/(med*len(a))**0.5
    in_sk = 0
    in_2sk = 0
    ma = max(a)
    nums = [0]*(ma + 1)
    for i in range(4000//k):
        nums[a[i]] += 1
        if med + sko >= a[i] >= med - sko:
            in_sk += 1
        if med + 2*sko >= a[i] >= med - 2*sko:
            in_2sk += 1
    count['sk'] = in_sk/(4000//k)*100
    count['2sk'] = in_2sk / (4000 // k) * 100
    for i in range(len(nums)):
        nums[i] = nums[i]/4000*k
    ind = []
    for i in range(len(nums)):
        ind.append(i/k)
    plt.bar(ind, nums, width=1/k)
    key = list(count.keys())
    val = list(count.values())
    for i in range(len(val)):
        print(key[i], round(val[i], 2))
    print()
    plt.minorticks_on()
    plt.grid(which='minor', color='#A9A9A9', linestyle=':', linewidth=0.5)
    plt.grid()
    if len(kas) == 1:
        puasson = []
        gauss = []
        for i in range(len(nums)):
            puasson.append((med**i)/(factorial(i))*2.7183**(-1*med))
            gauss.append(1/(sko*(2*3.14)**0.5)*2.7183**(-0.5*((i-med)/sko)**2))
        plt.plot(ind, puasson, color="#FF0000")
        plt.plot(ind, gauss, color="#32CD32")
        plt.legend(['puasson', 'gauss'])
        plt.show()
        meds = []
        sqmeds = []
        skos = []
        dmed = []
        s = 0
        c = 0
        for i in a:
            s += i
            c += 1
            sk = 0
            for i in range(c):
                sk += (a[i] - s/c)**2
            sk = (sk/c)**0.5
            dmed.append(sk/c**0.5)
            skos.append(sk)
            sqmeds.append((s/c)**0.5)
            meds.append(s/c)
        plt.plot(sqmeds)
        plt.plot(skos)
        plt.plot(dmed)
        plt.legend(['sqrmed', 'sko', 'dmed'])
        plt.minorticks_on()
        plt.grid(which='minor', color='#A9A9A9', linestyle=':', linewidth=0.5)
        plt.grid()
        plt.show()
        sk_m = [meds[0] - skos[0]]
        sk_p = [meds[0] - skos[0]]
        for i in range(1, len(meds)):
            sk_m.append(meds[i] - skos[i]/i**0.5)
            sk_p.append(meds[i] + skos[i]/i**0.5)
        plt.plot(meds, color="#FF0000")
        plt.plot(sk_m, color="#FFFF00")
        plt.plot(sk_p, color="#FFFF00")
        #plt.plot(0, 0, color="#FFFFFF")
        plt.minorticks_on()
        plt.grid(which='minor', color='#A9A9A9', linestyle=':', linewidth=0.5)
        plt.grid()

plt.show()