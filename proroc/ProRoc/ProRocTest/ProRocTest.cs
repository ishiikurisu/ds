using NUnit.Framework;
using ProRoc;
using System;

namespace ProRocTest
{
    [TestFixture]
    public class ProRocTest
    {

        [Test]
        public void TestSayHiFunction()
        {
            string output = ExampleStuff.SayHi("Joe");
            Assert.AreEqual("Hi Joe", output);
        }

        [Test]
        public void TestRocWeightConvertionWorks()
        {
            double[] input = new double[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
            double[] answer = Model.Roc(input);
            double[] correct = new double[]
            {
                0.29289,
                0.19289,
                0.14289,
                0.10956,
                0.08456,
                0.06456,
                0.04789,
                0.03361,
                0.02111,
                0.01000
            };

            for (int i = 0; i < input.Length; ++i)
            {
                Assert.True((answer[i] >= correct[i]*0.99) && (answer[i] <= correct[i] * 1.01));
            }
        }

        [Test]
        public void TestPrometheeModelWorksCorrectly()
        {
            string[] criteria = new string[]
            {
                "price",
                "comsuption",
                "comfort",
                "maintainance",
                "steering"
            };
            string[] actions = new string[]
            {
                "vw gol",
                "fiat uno",
                "chevy celta",
                "ford fiesta"
            };
            string[] correct = new string[]
            {
                "ford fiesta",
                "vw gol",
                "chevy celta",
                "fiat uno"
            };
            var weights = new double[] { 5, 4, 1, 3, 2 };
            var rankings = new double[][]
            {
                new double[] { 3, 2, 2, 1, 2 },
                new double[] { 4, 4, 1, 4, 1 },
                new double[] { 2, 3, 3, 2, 3 },
                new double[] { 1, 1, 4, 3, 4 }
            };

            var decisions = Model.Promethee(actions, criteria, weights, rankings);
            for (int i = 0; i < actions.Length; ++i)
            {
                Assert.AreEqual(correct[i], decisions[i]);
            }
        }
    }
}
