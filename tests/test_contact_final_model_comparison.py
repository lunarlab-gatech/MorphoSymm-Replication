import unittest
import os
import sys
import numpy as np

paper_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(paper_dir)

from paper.contact_final_model_comparison import generate_figure_4_right

class TestContactFinalModelComparison(unittest.TestCase):
    """
    Used to test that values plotted are correctly extracted
    from the csv files from the various directories.

    Note: The corresponding models with their metrics need
    to be copied into the proper directories for this to
    work. See the README.md of this repository for details.
    """

    def test_mihgnn_results(self):
        """
        Make sure our results are properly extracted.
        """

        # Get the extracted results
        df = generate_figure_4_right()

        # Filter out only those related to our model
        df = df[df['Model Type'] == "MI-HGNN"]

        # Set desired scores from each metric (directly from CSV)
        leg_0 = [0.9422018279723324, 0.935170555, 0.9409216197440856, 0.945855856,
                 0.9292235840098138, 0.9294136565408764, 0.939022302, 0.9439706942109056]
        leg_1 = [0.9309959993919372,0.9374760376181204,0.9323885619413274,0.944681331,
                 0.9316381779543564,0.9287626889828676,0.939777815,0.9482143799522024]
        leg_2 = [0.9422366682680758,0.9353183791877924,0.950477558,0.932681811,
                0.9170871756008874,0.933031389,0.9271497357085844,0.9433022041000394]
        leg_3 = [0.9295247571067394, 0.9338857539228737,0.9405202941471552,0.9403326868566312,
                 0.9166894709764988,0.9295666036406778,0.932631812,0.9375280026285132]
        avg = [0.9362398131847712,0.9354626813162626,0.941077008,0.940887921,
               0.9236596021353892,0.9301935844501648,0.9346454161859108,0.9432538202229152]
        acc = [0.8804949522018433, 0.8773993849754333, 0.8803967237472534, 0.8845410346984863,
                 0.8531096577644348, 0.8683673739433289, 0.8698036670684814, 0.8894924521446228]
        des_metrics = [leg_0, leg_1, leg_2, leg_3, avg, acc]

        # Extract scores for each metric
        metrics = ['Leg-LH\nF1', 'Leg-LF\nF1', 'Leg-RH\nF1', 'Leg-RF\nF1', 'Legs-Avg\nF1', 'State\nAcc']
        for i, m in enumerate(metrics):
            only_metric = df[df["metric"] == m]
            
            # Get all values of this metric
            actual_metric = []
            for index, row in only_metric.iterrows():
                actual_metric.append(row["Metric Score"])
            actual_metric.sort()

            # Get the desired metric
            des_met = des_metrics[i]
            des_met.sort()

            # Make sure it matches what we expect
            np.testing.assert_array_almost_equal(des_metrics[i], actual_metric, 9)

    def test_morpho_symm_results(self):
        """
        Test a small subset of the MorphoSymm
        results to make sure they are properly
        extracted.
        """

        # Get the extracted results
        df = generate_figure_4_right()

        # Filter out only those related to the ECNN
        df = df[df['Model Type'] == "ECNN"]

        # Set desired scores for ECNN state accuracy for all legs (directly from the 8 CSVs)
        des_acc = [0.7581040859222412, 0.7273257970809937, 0.7697378396987915, 0.7778831124305725,
                   0.8176508545875549, 0.808265745639801, 0.8478954434394836, 0.8009302616119385]
        des_acc.sort()

        # Get all values of test accuracy for all legs
        only_metric = df[df["metric"] == "State\nAcc"]
        only_metric = only_metric[only_metric["leg"] == "legs_avg"]
        actual_acc = []
        for index, row in only_metric.iterrows():
            actual_acc.append(row["Metric Score"])
        actual_acc.sort()

        # Make sure it matches what we expect
        np.testing.assert_array_almost_equal(des_acc, actual_acc, 9)


if __name__ == "__main__":
    unittest.main()