
import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        """pt1
        """
        averages = []
        for row in self.data: # creating a for loop to itetare through the data
            total_price = []
            for price in row[1:]:
               price = price.strip()
               if price and price.replace('.','', 1): # This line of code removes the spaces
                   price = float(price)
                   total_price.append(price)
            #    [float(price) for price in row if price != '.' and 1]
            # total_price.append(price)
            print(total_price)

              #gets the total averages 
            total_avg = sum(total_price) / len(total_price)
            averages.append(round(total_avg,3))
            # print(averages)
        return averages
        

# need to use stats on the median02 method
    def median02(self):
        median = []
        for row in self.data: 
            total_price = []
            for price in row[1:]:
               price = price.strip()
               if price and price.replace('.','', 1): 
                price = float(price)
                total_price.append(price)
                # In order to find the mediam of the total price, we need to use the median function, then append the overall median to the list.
            total_median = stats.median(total_price)
            median.append(total_median)
           
            # print(median) #using the print function to check if it's giving the correct results.
        return median
        

# stddev03 is for standard deviation
    def stddev03(self):
        standard_deviation = []
        for row in self.data: 
            total_price = []
            for price in row[1:]:
               price = price.strip()
               if price and price.replace('.','', 1): 
                price = float(price)
                total_price.append(price)
                # Using the stdev function to get the standard deviation and the round function to give it to the third decimal. 
            updated_stddv = stats.stdev(total_price)
            standard_deviation.append(round(updated_stddv, 3))
           
            # print(standard_deviation) 
        return standard_deviation
