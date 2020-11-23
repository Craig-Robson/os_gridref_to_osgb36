import pandas
import numpy
from osgr_to_osgb36_data import corrections

input_file = '/home/craig/Downloads/kittiwake_colinies_2000.csv'
output_file = '/home/craig/Downloads/kittiwake_colinies_2000_coords.csv'

data = pandas.read_csv(input_file, low_memory=False)

# create new fields to store new coordinates
data['e'] = numpy.nan
data['n'] = numpy.nan


i = 0
for index, row in data.iterrows():
   
    if isinstance(row['StartGrid'], str):

        print(row['StartGrid'])
        correction_e = corrections[row['StartGrid'][:2]]['E']
        correction_n = corrections[row['StartGrid'][:2]]['N']

        row['EASTING'] = row['StartGrid'][2:5]+str('0')
        row['NORTHING'] = row['StartGrid'][5:9]+str('0')
        print('------------')
        print(row['EASTING'])
        print(row['NORTHING'])
        print('------------')
        e = str(row['EASTING']).replace('.0','')
        n = str(row['NORTHING']).replace('.0','')

        while len(e) < 4:
            e = '0' + e
        
        while len(n) < 4:
            n = '0' + n

        e = e + '0'
        n = n + '0'

        e = correction_e + e
        n = correction_n + n

        data.at[index,'e'] = e
        data.at[index,'n'] = n

# write output file
data.to_csv(output_file)
    

