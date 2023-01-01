import pyrankvote, DD_RCV_data
from pyrankvote import Candidate, Ballot


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
            ballot = Ballot([DD_RCV_data.Shaan, DD_RCV_data.Harry])
        elif vote == 'Harry, Shaan':
            ballot = Ballot([DD_RCV_data.Harry, DD_RCV_data.Shaan])

    elif election == 'Builder_Co-Steward':
        if vote == 'Tim, Joshua, Amanda':
            ballot = Ballot([DD_RCV_data.Tim, DD_RCV_data.Joshua, DD_RCV_data.Amanda])
        elif vote == 'Tim, Amanda, Joshua':
            ballot = Ballot([DD_RCV_data.Tim, DD_RCV_data.Amanda, DD_RCV_data.Joshua])
        elif vote == 'Joshua, Tim, Amanda':
            ballot = Ballot([DD_RCV_data.Joshua, DD_RCV_data.Tim, DD_RCV_data.Amanda])
        elif vote == 'Joshua, Amanda, Tim':
            ballot = Ballot([DD_RCV_data.Joshua, DD_RCV_data.Amanda, DD_RCV_data.Tim])
        elif vote == 'Amanda, Tim, Joshua':
            ballot = Ballot([DD_RCV_data.Amanda, DD_RCV_data.Tim, DD_RCV_data.Joshua])
        elif vote == 'Amanda, Joshua, Tim':
            ballot = Ballot([DD_RCV_data.Amanda, DD_RCV_data.Joshua, DD_RCV_data.Tim])

    elif election == 'Gatherings_WG-Lead':
        if vote == 'Rebeca, Ibtehaj, Fernando':
            ballot = Ballot([DD_RCV_data.Rebeca, DD_RCV_data.Ibtehaj, DD_RCV_data.Fernando])
        elif vote == 'Rebeca, Fernando, Ibtehaj':
            ballot = Ballot([DD_RCV_data.Rebeca, DD_RCV_data.Fernando, DD_RCV_data.Ibtehaj])
        elif vote == 'Ibtehaj, Rebeca, Fernando':
            ballot = Ballot([DD_RCV_data.Ibtehaj, DD_RCV_data.Rebeca, DD_RCV_data.Fernando])
        elif vote == 'Ibtehaj, Fernando, Rebeca':
            ballot = Ballot([DD_RCV_data.Ibtehaj, DD_RCV_data.Fernando, DD_RCV_data.Rebeca])
        elif vote == 'Fernando, Rebeca, Ibtehaj':
            ballot = Ballot([DD_RCV_data.Fernando, DD_RCV_data.Rebeca, DD_RCV_data.Ibtehaj])
        elif vote == 'Fernando, Ibtehaj, Rebeca':
            ballot = Ballot([DD_RCV_data.Fernando, DD_RCV_data.Ibtehaj, DD_RCV_data.Rebeca])

    elif election == 'Governance_WG-Lead':
        if vote == 'Yes':
            ballot = Ballot([DD_RCV_data.Aditya_Yes])
        elif vote == 'No,':
            ballot = Ballot([DD_RCV_data.Aditya_No])

    elif election == 'Grants_WG-Lead':
        if 'Yes' in vote:
            ballot = Ballot([DD_RCV_data.Amanda_Yes])
        elif 'No' in vote:
            ballot = Ballot([DD_RCV_data.Amanda_No])
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
    print(repeat_codes)
    print(invalid_codes)
    return ballots


def conduct_election(candidates,ballots):
    election_result = pyrankvote.instant_runoff_voting(candidates,ballots)
    return election_result