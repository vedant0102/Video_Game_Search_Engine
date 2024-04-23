from bs4 import BeautifulSoup
from pathlib import Path
import pandas as pd


class HtmlToJson:
    def __init__(self):
        # Initialize an empty list to store data extracted from HTML files
        self.data = []
        # Specify the output JSON file path
        self.output_filename = "C:/Illinois Tech/Sem 2/Information Retrival/Video_Game_Crawler/Video_Game_Indexer/data.json"

    def htmlFileProcessor(self, html_dir):
        """
        Process HTML files in the specified directory.

        Parameters:
        - html_dir (str): Directory containing HTML files to be processed.
        """
        # Iterate over all files in the specified directory
        for file_path in Path(html_dir).iterdir():
            print(file_path)  # Print the current file path for debugging purposes
            # Check if the file is an HTML file
            if file_path.suffix == ".html":
                # Open the HTML file for reading
                with open(file_path, "r", encoding="utf-8") as f:
                    # Read the contents of the HTML file
                    contents = f.read()
                    # Parse the HTML content using BeautifulSoup
                    soup = BeautifulSoup(contents, 'html.parser')
                    # Check if the HTML contains a title with the specified id
                    if soup.find("h1", id="firstHeading") is not None:
                        # Extract the title text
                        title = soup.find("h1", id="firstHeading").get_text()
                        # Extract text from all paragraphs within the main content area
                        paragraphs = [p.get_text() for p in soup.select("div.mw-content-ltr p")]
                        # Join the paragraphs into a single string and replace newline characters with spaces
                        content = " ".join(paragraphs).replace("\n", " ")
                        # Append the title and content to the data list as a dictionary
                        self.data.append({"title": title, "content": content})

    def jsonMaker(self):
        """
        Convert processed data to JSON format and save it to a file.
        """
        # Convert the list of dictionaries to a pandas DataFrame
        data_json = pd.DataFrame(self.data)
        # Save the DataFrame to a JSON file with specified orientation
        data_json.to_json(self.output_filename, orient='records')


if __name__ == "__main__":
    # Specify the directory containing HTML files to be processed
    html_directory = "C:/Illinois Tech/Sem 2/Information Retrival/Video_Game_Crawler/Video_Game_Crawler/webpages"

    # Create an instance of the HtmlToJson class
    parser = HtmlToJson()
    # Process HTML files in the specified directory
    parser.htmlFileProcessor(html_directory)
    # Convert processed data to JSON format and save it to a file
    parser.jsonMaker()
