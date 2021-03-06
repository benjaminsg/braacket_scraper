from config import leagues

class Ranking:
    def __init__(self, id, name, league):
        # id taken from Braacket player page
        self.id = id
        # name is name that will display in all output formats
        self.name = name
        # league is the league the ranking is in
        self.league = league

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
    
NewEnglandMelee = leagues.NewEnglandMelee
WashingtonMelee = leagues.WashingtonMelee
    
FallWinter2022_NE = Ranking('7EADD432-EF78-40BD-A179-7D797CE9F37D', 'Fall 2021/Winter 2022', NewEnglandMelee)
InterRanking_NE = Ranking('7FA7ED91-C78A-4C46-914F-F8F444EBADA3', 'Inter-Ranking Period', NewEnglandMelee)
FallWinter2020_NE = Ranking('191499FD-F577-49BD-B341-DE9BC22EB813', 'Fall 2019/Winter 2020', NewEnglandMelee)
SpringSummer2019_NE = Ranking('3B26CC90-A536-4F78-937D-8287D30608F3', 'Spring 2019/Summer 2019', NewEnglandMelee)
FallWinter2019_NE = Ranking('CE294EEF-A3D0-481D-A6EB-BEB8FEFF9738', 'Fall 2019/Winter 2020', NewEnglandMelee)
SpringSummer2018_NE = Ranking('4CA75C29-6660-4110-99CF-A291D0F2D62D', 'Spring 2018/Summer 2018', NewEnglandMelee)
FallWinter2018_NE = Ranking('274676F3-7928-4C9F-B1C0-7ECDD0ADE0CA', 'Fall 2017/Winter 2018', NewEnglandMelee)

WinterSpring2022_WA = Ranking('2E2CC2DE-78E7-45FD-B127-ACEDCDF98D36', 'Winter/Spring 2022', WashingtonMelee)

NE_all_seasons = [FallWinter2022_NE, InterRanking_NE, FallWinter2020_NE, SpringSummer2018_NE, FallWinter2019_NE,
                  FallWinter2019_NE, SpringSummer2018_NE, FallWinter2018_NE]

WA_all_seasons = [WinterSpring2022_WA]