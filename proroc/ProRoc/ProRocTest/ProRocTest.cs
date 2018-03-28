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
    }
}
