import unittest
import csv

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_loop_data(self):
        dataPath='/'
        loopFile='loopSamples.txt'

        with open(loopFile, 'rU') as fin:
            cin = csv.DictReader(fin)
            sampleData= [row for row in cin]
        
        detectorid=''
        starttime=''
        volume=''
        speed=''
        occupancy=''
        status=''
        dqflags=''

        #get vals from each line in sample data.  try to get same vals from database
        for sample in sampleData:
            #get data from sample
            sampleDetectorid = sample['detectorid']
            sampleStarttime = sample['starttime']
            sampleVolume = sample['volume']
            sampleSpeed = sample['speed']
            sampleOccupancy = sample['occupancy']
            sampleStatus = sample['status']
            sampleDqflags = sample['dqflags']

            #get data from db
            dbDetectorid = sample['detectorid']
            dbStarttime = sample['starttime']
            dbVolume = sample['volume']
            dbSpeed = sample['speed']
            dbOccupancy = sample['occupancy']
            dbStatus = sample['status']
            dbDqflags = sample['dqflags']

            self.assertEqual(sampleDetectorid, dbDetectorid)
            self.assertEqual(sampleStarttime, dbStarttime)
            self.assertEqual(sampleVolume, dbVolume)
            self.assertEqual(sampleSpeed, dbSpeed)
            self.assertEqual(sampleSpeed, dbSpeed)

if __name__ == '__main__':
    unittest.main()