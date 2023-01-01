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


def submitted_code(submission):
    code_submission = submission.split(',')
    code = code_submission[1]
    return code


def submitted_vote(submission,election):
    vote_submission = submission.split('"')
    if election == 'Champion_Co-Steward':
        vote = vote_submission[5]
    elif election == 'Builder_Co-Steward':
        vote = vote_submission[3]
    elif election == 'Gatherings_WG-Lead':
        vote = vote_submission[7]
    elif election == 'Governance_WG-Lead':
        vote = submission[94:97]
    elif election == 'Grants_WG-Lead':
        vote = submission[97:101]
    return vote


def vote_assignment(vote,election):
    if election == 'Champion_Co-Steward':
        if vote == 'Shaan, Harry':
            ballot = Ballot([Shaan, Harry])
        elif vote == 'Harry, Shaan':
            ballot = Ballot([Harry, Shaan])

    elif election == 'Builder_Co-Steward':
        if vote == 'Tim, Joshua, Amanda':
            ballot = Ballot([Tim, Joshua, Amanda])
        elif vote == 'Tim, Amanda, Joshua':
            ballot = Ballot([Tim, Amanda, Joshua])
        elif vote == 'Joshua, Tim, Amanda':
            ballot = Ballot([Joshua, Tim, Amanda])
        elif vote == 'Joshua, Amanda, Tim':
            ballot = Ballot([Joshua, Amanda, Tim])
        elif vote == 'Amanda, Tim, Joshua':
            ballot = Ballot([Amanda, Tim, Joshua])
        elif vote == 'Amanda, Joshua, Tim':
            ballot = Ballot([Amanda, Joshua, Tim])

    elif election == 'Gatherings_WG-Lead':
        if vote == 'Rebeca, Ibtehaj, Fernando':
            ballot = Ballot([Rebeca, Ibtehaj, Fernando])
        elif vote == 'Rebeca, Fernando, Ibtehaj':
            ballot = Ballot([Rebeca, Fernando, Ibtehaj])
        elif vote == 'Ibtehaj, Rebeca, Fernando':
            ballot = Ballot([Ibtehaj, Rebeca, Fernando])
        elif vote == 'Ibtehaj, Fernando, Rebeca':
            ballot = Ballot([Ibtehaj, Fernando, Rebeca])
        elif vote == 'Fernando, Rebeca, Ibtehaj':
            ballot = Ballot([Fernando, Rebeca, Ibtehaj])
        elif vote == 'Fernando, Ibtehaj, Rebeca':
            ballot = Ballot([Fernando, Ibtehaj, Rebeca])

    elif election == 'Governance_WG-Lead':
        if vote == 'Yes':
            ballot = Ballot([Aditya_Yes])
        elif vote == 'No,':
            ballot = Ballot([Aditya_No])

    elif election == 'Grants_WG-Lead':
        if 'Yes' in vote:
            ballot = Ballot([Amanda_Yes])
        elif 'No' in vote:
            ballot = Ballot([Amanda_No])
    return ballot


def read_ballots(votes_file,election,valid_codes):
    ballots = []
    cast_codes = []
    repeat_codes = []
    invalid_codes = []
    with open(votes_file) as f:
        for line in f:
            code = submitted_code(line)
            vote = submitted_vote(line,election)
            if code in valid_codes:
                if code not in cast_codes:
                    cast_codes.append(code)
                    ballots.append(vote_assignment(vote,election))
                else:
                    repeat_codes.append(code)
            else:
                invalid_codes.append(code)
    return ballots


def conduct_election(candidates,ballots):
    election_result = pyrankvote.instant_runoff_voting(candidates,ballots)
    return election_result

valid_codes = sorted_codes
votes_file = votes_file
election = 'Governance_WG-Lead'
candidates = governance_wg_lead_candidates

ballots = read_ballots(votes_file, election, valid_codes)

results = conduct_election(candidates,ballots)
print(f'\n{results}')