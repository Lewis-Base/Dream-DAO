import DD_RCV, DD_RCV_data

'''
Elections=
Champion_Co-Steward
Builder_Co-Steward
Gatherings_WG-Lead
Governance_WG-Lead
Grants_WG-Lead

Candidates=
champion_co_steward_candidates
builder_co_steward_candidates
gatherings_wg_lead_candidates
governance_wg_lead_candidates
grants_wg_lead_candidates
'''

valid_codes = DD_RCV_data.sorted_codes
votes_file = DD_RCV_data.votes_file
election = 'Champion_Co-Steward'
candidates = DD_RCV_data.champion_co_steward_candidates

ballots = DD_RCV.read_ballots(votes_file, election, valid_codes)

results = DD_RCV.conduct_election(candidates,ballots)
print(f'\n{results}')