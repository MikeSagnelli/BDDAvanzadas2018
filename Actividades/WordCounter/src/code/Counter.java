package code;

// Import libraries for reading files, and for implementing hash table.
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Counter{

	private Map<String, Integer> dictionary; // Hash table for running code in O(n) complexity
	private BufferedReader br; // Buffered reader for reading next line in a text file
	private FileReader fr; // File reader for openning a file
	
	private static final String FILE_NAME = ""; // Edit with default route for a file
	
	// Default constructor, when no file is specified use FILE_NAME default route
	public Counter() {
		this.dictionary = new HashMap<String, Integer>();
		this.fr = null;
		this.br = null;
		
		String line; // Temporal line in br
		try {
			this.fr = new FileReader(FILE_NAME);
			this.br = new BufferedReader(fr);
			int i = 0;
			String[] wordsInLine; // Array for splitting the line into words
			while((line = br.readLine()) != null){
				wordsInLine = line.split(" ");
				for(String word : wordsInLine) {
					this.dictionary.put(word, i); // Check if the word was already in dictionary, replace or add
					i++;
				}
			}
		}
		catch(IOException e) {
			e.printStackTrace();
		}
		finally {
			try {
				if(br != null) {
					this.br.close();
				}
				if(fr != null) {
					this.fr.close();
				}
			}
			catch(IOException ex) {
				ex.printStackTrace();
			}
		}
		
	}
	
	//Specify route for a file
	public Counter(String fileName) {
		this.dictionary = new HashMap<String, Integer>();
		this.fr = null;
		this.br = null;
		
		String line;
		try {
			this.fr = new FileReader(fileName);
			this.br = new BufferedReader(fr);
			String[] wordsInLine;
			while((line = br.readLine()) != null){
				wordsInLine = line.split(" ");
				for(String word : wordsInLine) {
					if(this.dictionary.containsKey(word)) {
						int value = this.dictionary.get(word);
						this.dictionary.put(word, value + 1);
					}
					else {
						this.dictionary.put(word, 1);
					}
				}
			}
		}
		catch(IOException e) {
			e.printStackTrace();
		}
		finally {
			try {
				if(br != null) {
					this.br.close();
				}
				if(fr != null) {
					this.fr.close();
				}
			}
			catch(IOException ex) {
				ex.printStackTrace();
			}
		}
	}
	
	// Just print the output by printing the hash table
	public void printOutput() {
		for (String key : this.dictionary.keySet()) {
			System.out.println("Key: " + key + " is in file " + this.dictionary.get(key) + " times.");
		}
	}
}
