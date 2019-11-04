import math





class statistik:

    

    def __init__(self, set, intervalls):

        self.set = sorted(set)
        self.intervalls = intervalls
        



    def calculate_min(sorted_set):
        return sorted_set[0]

    def calculate_max(sorted_set):
        return sorted_set[len(sorted_set)-1]


    def calculate_range(sorted_set):

        return sorted_set[len(sorted_set)-1] - sorted_set[0]

    def calculate_mean(set):

        mean = 0
        n = len(set) # number of elements in set

        for value in set:
            mean += value
    
        return mean / n
    # QUANTILES
    ####


    def calculate_p_quantile(p, sorted_set):

        n = len(sorted_set) # number of elements in set
    
        try:
            # n * p is integer
            return 0.5 * (sorted_set[(n*p)-1] + sorted_set[((n*p)+1)-1])
        except TypeError:
            # n * p is not integer
            return sorted_set[int(math.floor(n*p+1))-1]
    


    def calculate_median(sorted_set):
        return calculate_p_quantile(0.5, sorted_set)

    def calculate_first_quartile(sorted_set):

        return calculate_p_quantile(0.25, sorted_set)

    def calculate_third_quartile(sorted_set):

        return calculate_p_quantile(0.75, sorted_set)



    ####


    def calculate_variance(set):

        x_bar = calculate_mean(set)
        n = len(set)

        variance = 0

        for value in set:
            variance += ((value - x_bar) * (value - x_bar))

        return variance / (n-1)

    def calculate_standard_deviation(set):

        return math.sqrt(calculate_variance(set))


    def calculate_interquartile_range(sorted_set):

        n = len(sorted_set)

        return sorted_set[math.floor(n * 0.75) -1] - sorted_set[math.floor(n * 0.25) -1] 




    def count_occurences_of_data_in_intervalls(intervalls, set):
        n = 0
        numlist = []

        for intervall in intervalls:
            for datapoint in range(len(set)):
                if (intervall[0] <= set[datapoint] and set[datapoint] <= intervall[1]):
                    n += 1
            
            numlist.append(n)
            n = 0
        
        return numlist




    set = [12.7,8.8,37.3,32.2,30.4,20.1,36.1,7.7,3.6,51.5,33.0,22.4,38.6,24.8,50.6,38.6,36.4,54.8,49.4,59.6,53.2,24.0,25.4]

    intervalls = [[0,9], [10,19], [20,29], [30,39], [40, 49], [50, 69], [70, 100]]

    datapoints_in_intervalls = []

    sorted_set = sorted(set)

    print("MEDIAN: " + str(calculate_median(sorted_set)))
    print("MEAN: " + str(calculate_mean(set)))
    print("RANGE: " + str(calculate_range(sorted_set)))
    print("VARIANCE: " + str(calculate_variance(set)))
    print("STANDARD DEVIATION: " + str(calculate_standard_deviation(set)))
    print("INTERQUARTILE RANGE: " + str(calculate_interquartile_range(sorted_set)))





    print("BOXPLOT")
    print("--------------")

    print("MIN: " + str(calculate_min(sorted_set)))

    print("1ST QUARTILE: " + str(calculate_p_quantile(0.25,sorted_set)))
    print("2ND QUARTILE (MEDIAN): " + str(calculate_median(sorted_set)))
    print("3RD QUARTILE: " + str(calculate_p_quantile(0.75,sorted_set)))

    print("MAX: " + str(calculate_max(sorted_set)))