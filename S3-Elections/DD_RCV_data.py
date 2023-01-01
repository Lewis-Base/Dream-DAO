import pyrankvote
from pyrankvote import Candidate, Ballot

Shaan = Candidate("Shaan")
Harry = Candidate("Harry")
champion_co_steward_candidates = [Shaan, Harry]

Tim = Candidate("Tim")
Joshua = Candidate("Joshua")
Amanda = Candidate("Amanda")
builder_co_steward_candidates = [Tim, Joshua, Amanda]

Rebeca = Candidate("Rebeca")
Ibtehaj = Candidate("Ibtehaj")
Fernando = Candidate("Fernando")
gatherings_wg_lead_candidates = [Rebeca, Ibtehaj, Fernando]

Aditya_Yes = Candidate("Aditya_Yes")
Aditya_No = Candidate("Aditya_No")
governance_wg_lead_candidates = [Aditya_Yes, Aditya_No]

Amanda_Yes = Candidate("Amanda_Yes")
Amanda_No = Candidate("Amanda_No")
grants_wg_lead_candidates = [Amanda_Yes, Amanda_No]

def ingest_codes(string):
    codes = string.replace("\n", "', '")
    return codes

raw_codes = '''

'''

#print(ingest_codes(raw_codes))

unsorted_codes = []
sorted_codes = sorted(unsorted_codes)
votes_file = 'dream-dao-election-season-3.csv'