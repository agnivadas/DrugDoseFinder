import rdflib
from fuzzywuzzy import process
import os



# Ensure the script's directory is set as the working directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)




def load_rdf_files(rdf_files):
    """Loads RDF files into an RDF graph and returns the graph."""
    g = rdflib.Graph()
    for rdf_file in rdf_files:
        if os.path.exists(rdf_file):
            g.parse(rdf_file, format="xml")  # Parse RDF file
        else:
            print(f"Warning: File {rdf_file} not found.")
    return g

def extract_drug_names(g, hasName):
    """Extracts drug names from the RDF graph and returns them as a list."""
    return [str(o) for o in g.objects(predicate=hasName)]

def search_for_drug_name(drug_names, search_name):
    """Search for a drug name and return the matches with their scores."""
    return process.extract(search_name, drug_names, limit=None)

def filter_matches(matches):
    """Filters the matches to only include those with a score above 80."""
    return [(match[0], match[1]) for match in matches if match[1] > 80]

def display_filtered_matches(filtered_matches):
    """Displays the filtered matches to the user and returns the selected choice."""
    print("\nMatches (choose the drug from below and enter number of it):\n")
    for i, match in enumerate(sorted(filtered_matches, key=lambda x: x[1], reverse=True)):
        print(f"{i + 1}. {match[0]} ")

    try:
        choice = int(input("\nChoose a match number: ")) - 1
        if 0 <= choice < len(filtered_matches):
            return filtered_matches[choice][0]
        else:
            print("Invalid choice. Please select a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    return None

def fetch_dose_information(g, chosen_match, hasName):
    """Fetches and displays dose information for the chosen drug."""
    best_match_uri = None
    for subject in g.subjects(predicate=hasName, object=rdflib.Literal(chosen_match)):
        best_match_uri = subject
        print(f"Drug URI: {subject}")
        
        dose_content = None
        for dose_object in g.objects(subject=subject, predicate=rdflib.URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#hasDose")):
            dose_content = dose_object
            print("\nDose Information:")
            print(dose_content)
            break  # Only one rdf:hasDose is expected, so we break after fetching it.

        if dose_content is None:
            print("\nNo dose information (rdf:hasDose) found for the selected drug.")

def main():
    # List of RDF files to be loaded
    rdf_files = ["database1.rdf", "database2.rdf"]  # Example file names

    # Define the URI for ex:hasName and namespace
    EX = rdflib.Namespace("http://example.org/")
    hasName = EX.hasName

    # Load RDF files into the graph
    g = load_rdf_files(rdf_files)

    # Extract drug names from the graph
    drug_names = extract_drug_names(g, hasName)

    # Search for a drug name
    while True:
        # Search for a drug name
        search_name = input("Enter the drug name to search: ").strip()  # Get drug name from user input

        # Get all matches with their scores
        matches = search_for_drug_name(drug_names, search_name)

        # Filter matches with scores above 80
        filtered_matches = filter_matches(matches)

        # Check if any matches were found above score 80
        if filtered_matches:
            chosen_match = display_filtered_matches(filtered_matches)

            if chosen_match:
                print(f"\nYou selected: {chosen_match}")
                # Retrieve and display the dose information for the selected match
                fetch_dose_information(g, chosen_match, hasName)
        else:
            print("No matches found. Raise issue will update the database.")
# Run the main function
if __name__ == "__main__":
    main()
