final color WHITE = #FFFFFF;
String[] committees;

/* FILE IO */

String[] loadCommittees() {
	BufferedReader reader = createReader("./data/committees.txt");
	StringList outlet = new StringList();
	String line = null;

	try {
		while ((line = reader.readLine()) != null) {
			outlet.append(line);
		}
		reader.close();
	} catch (IOException e) {
		e.printStackTrace();
	}

	return outlet.array();
}

/* MAIN SECTION */


void setup() {
	size(1300, 800);
	committees = loadCommittees();
}

void draw() {
	background(WHITE);

	exit();
}
