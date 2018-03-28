using NUnit.Framework;
using ProRoc;

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
    }
}
