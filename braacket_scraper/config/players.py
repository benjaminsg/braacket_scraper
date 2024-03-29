from config import leagues

class Player:
    def __init__(self, id, name, league):
        # id taken from Braacket player page
        self.id = id
        # tag is name that will display in all output formats
        self.name = name
        # league is the league the player is in
        self.league = league
        
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

NewEnglandMelee = leagues.NewEnglandMelee
WashingtonMelee = leagues.WashingtonMelee

# create NE players
Abel = Player('F1198D7F-034A-4C32-B61C-8525757DBAAC', 'Abel', NewEnglandMelee)
Ac3r = Player('8515AD5F-DE0C-4A15-9A70-7DB27066967F', 'ac3r', NewEnglandMelee)
AdmiralZhao = Player('2FBD0DB5-20A1-4E19-BCE7-64EA0588023A', 'Admiral Zhao', NewEnglandMelee)
Alt = Player('CE3A82DF-DDF2-4858-A007-D51F8C227CA5', 'Alt', NewEnglandMelee)
Alte = Player('56C9A7ED-BFFD-4EC2-9FDE-500290341D30', 'Alte', NewEnglandMelee)
Analog = Player('3927BB05-304F-4C60-AB08-8AEF00DC49C2', 'analog', NewEnglandMelee)
Ant = Player('5DBCC342-92B6-40C6-AFBF-66933EF41379', 'Ant', NewEnglandMelee)
Arcade = Player('42790139-FFF0-48E5-90ED-7F3500F2C805', 'Arcade', NewEnglandMelee)
Artelind = Player('9CB48DEB-E0C6-428F-B74D-8DF4395C77BF', 'Artelind', NewEnglandMelee)
Arty = Player('CEBCAD46-A933-4EA6-92F1-B9C85D5C71F2', 'Arty', NewEnglandMelee)
AwesomeVideoGames = Player('23F2D11B-9DA7-4FEB-9EC9-640EB1DA57D0', 'Awesome Video Games', NewEnglandMelee)
Bank = Player('E85EE0F4-C335-4A1C-A569-BE69C1675BAA', 'Bank', NewEnglandMelee)
Bekvin = Player('0ED0B111-D617-4E32-B2CA-9004A4BAAA22', 'Bekvin', NewEnglandMelee)
Ben = Player('D8BDA006-37EB-402B-B87D-40AE4725C394', 'Ben', NewEnglandMelee)
BLAK = Player('2328E264-DFBF-418C-970B-979F838361E2', 'BLAK', NewEnglandMelee)
Blizz = Player('4C3FC2FB-53CD-46F1-AF9F-32332D8882AC', 'Blizz', NewEnglandMelee)
Bonfire10 = Player('C9B8492C-13D2-4D31-A7ED-A79821206267', 'bonfire10', NewEnglandMelee)
BonkCushy = Player('10562558-14C6-4D76-B65C-212CE682E0F1', 'BonkCushy', NewEnglandMelee)
Brub = Player('1136C70F-C32E-4A38-9A48-A38BB5DA1F08', 'Brub', NewEnglandMelee)
Catfish = Player('E7660D46-C947-4A03-8B63-5AB7C8D2174D', 'Catfish', NewEnglandMelee)
Clutch = Player('03C03D58-1C4F-4F2D-B1D8-BD622231E829', 'Clutch', NewEnglandMelee)
Cocoa_ = Player('2FCDB4A8-D43F-421E-B980-54F0668E6320', 'Cocoa_', NewEnglandMelee)
Conflict = Player('38A911E4-2509-47A1-8479-C9BD87DFB119', 'Conflict', NewEnglandMelee)
Coolslice = Player('583438BD-F9A1-413A-8F77-DEF3820143F0', 'Coolslice', NewEnglandMelee)
Cupofwater = Player('C8F72208-282F-4D3D-8E50-794DF3B55ECF', 'cupofwater', NewEnglandMelee)
Dad = Player('2C2FFDE9-4E62-443C-9A9E-94D7CBB4AE64', 'Dad', NewEnglandMelee)
Deadstock = Player('7B7CA495-2CFE-4CA2-B249-02FF3833DBB7', 'Deadstock', NewEnglandMelee)
Dour = Player('68A7DE4A-F72F-4BCC-85B8-FE64C165C291', 'Dour', NewEnglandMelee)
DrLame = Player('161B23E2-286E-427F-809F-D2F6FC60255D', 'Dr. Lame', NewEnglandMelee)
DrLobster = Player('6B2BEB69-DCE1-4095-BFED-4F3205CF3CDB', 'DrLobster', NewEnglandMelee)
Dudutsai = Player('A4CB0944-7C18-4BF6-BF2A-AAD9F55F7392', 'dudutsai', NewEnglandMelee)
Dulcetones = Player('C249444C-0A8D-4014-8363-E8C87B760066', 'Dulcetones', NewEnglandMelee)
Electroman = Player('BAB54F38-444F-4ADE-8D79-EC7D232D90E9', 'Electroman', NewEnglandMelee)
Ember = Player('10F61347-8632-448F-AAD5-AFB8F7F72C43', 'Ember', NewEnglandMelee)
Epoodle = Player('F7441D6E-6DB4-4BBB-8F3E-B2EB0DFA533B', 'Epoodle', NewEnglandMelee)
ETHANBURKE = Player('1787A0DC-2C4A-4E4A-9CD4-D1649E9855F9', 'ETHAN BURKE', NewEnglandMelee)
Eveningstar = Player('F3FCF46A-29B7-4F2F-A02D-A93C7E948144', 'eveningstar', NewEnglandMelee)
Fats = Player('7EDC6998-3DF3-4682-9F29-D7BE8BF29D16', 'Fats', NewEnglandMelee)
FreeSSBM = Player('0411F12F-D6F2-41EF-AC41-66CFF5256A28', 'FreeSSBM', NewEnglandMelee)
Frosty = Player('716F783D-A4BF-4C99-96A5-56822659348B', 'Frosty', NewEnglandMelee)
Fruity = Player('30A150C5-8169-4068-98DA-996A6274E847', 'Fruity', NewEnglandMelee)
FutureShock = Player('5CD3DDFC-6380-4395-8DF7-590D498437E2', 'Future Shock', NewEnglandMelee)
Glock = Player('1FE504AF-EE8C-4426-AEDD-2EF99F053B17', 'glock in my toyota', NewEnglandMelee)
Glory = Player('CDE4E32C-1388-40DC-9F29-3C786BAEE40C', 'Glory', NewEnglandMelee)
Golden = Player('CC999B81-122C-47AA-8B5A-A1FDABFEAD41', 'Golden', NewEnglandMelee)
Greenstach = Player('0267F6B4-223B-4D0D-B0AB-3B7084B37AB7', 'Greenstach', NewEnglandMelee)
Guex = Player('1AE48CD4-CCAB-4B99-8677-555C32A99A6B', 'Guex', NewEnglandMelee)
GWM420 = Player('20D39883-8B90-4E8A-9136-363E53E1CE37', 'GWM420', NewEnglandMelee)
Hexjo = Player('D663F90B-0A81-4D27-B32B-ED83F2395972', 'Hexjo', NewEnglandMelee)
Hysteric = Player('3576ECE4-EACF-4E83-995C-F40FB232EADD', 'Hysteric', NewEnglandMelee)
IOA = Player('4A825404-F98D-4AD7-A37F-44A0EB7EA62B', 'IOA', NewEnglandMelee)
JNaut = Player('1D1EEAFE-A49D-49FE-81FD-68A1D6923E8C', 'JNaut', NewEnglandMelee)
Jwilli = Player('C551AE24-9E46-491D-A256-D8B48C7A2BD6', 'Jwilli', NewEnglandMelee)
Kacey = Player('D861C5C8-2B42-4AB6-8649-6256E0EEF6E5', 'Kacey', NewEnglandMelee)
Kalvar = Player('C2069576-DB5B-42E0-9C4B-31182802A60F', 'Kalvar', NewEnglandMelee)
Keto = Player('443B05FC-FCF5-4200-AF36-BD6750498C65', 'Keto', NewEnglandMelee)
Khan = Player('1C938488-41B9-4007-81C0-E1C46E9BA742', 'Khan', NewEnglandMelee)
Kikoho = Player('27CF9E7D-F2DE-4126-B620-3D76454E463C', 'kikoho', NewEnglandMelee)
Kota = Player('4A441F9A-DE7E-4749-8E47-DFCBB388F23D', 'Kota', NewEnglandMelee)
KPeace = Player('EC6714D8-2B2B-4D90-8661-6CD2003BF31A', 'KPeace', NewEnglandMelee)
Kraft = Player('0CDB11B1-BCC3-4027-90F2-D74F1A9A5668', 'Kraft', NewEnglandMelee)
Krakhead = Player('01B96331-367C-42E4-B3A9-5198F728228D', 'Krakhead', NewEnglandMelee)
Kuni = Player('5D3BB58F-82D1-453A-8806-7BEE955C6230', 'Kuni', NewEnglandMelee)
L33b = Player('2CEACB53-351C-4697-9C94-0F08CC6B7828', 'L33b', NewEnglandMelee)
L8er = Player('D5811987-108F-4197-AC40-9779688DBA7E', 'L8er', NewEnglandMelee)
Lamdin = Player('3E5CBCCB-C3F7-4FE2-BC7F-B812DC3EE621', 'Lamdin', NewEnglandMelee)
Lio = Player('10C85F81-C7B5-44FF-AD81-E51658967E2D', 'Lio', NewEnglandMelee)
Loadspiller = Player('EAE5E0CC-99FF-49EB-8424-142348454761', 'Loadspiller', NewEnglandMelee)
Louis = Player('4C2B18BA-75A9-45ED-A8B6-8D891297E00A', 'Louis', NewEnglandMelee)
Makari = Player('40E8C7E0-FF26-44B7-9225-FD3D257CAC10', 'Makari', NewEnglandMelee)
MEAT = Player('0D8C1F36-D79B-4FEF-91DE-5963AC99D13D', 'MEAT', NewEnglandMelee)
Meep = Player('0C1E5B62-12A1-43FB-B6AB-B5FAB1651020', 'meep', NewEnglandMelee)
Mike = Player('AC78EC1F-AD14-4C0B-A251-65EF2666D605', 'Mike', NewEnglandMelee)
MommyDaddy = Player('745B344A-7D01-471F-BEDD-7709B8CA19D2', 'MommyDaddy', NewEnglandMelee)
MOOP = Player('BBB96C16-AA44-4A05-965A-0BB8A7FDE602', 'MOOP', NewEnglandMelee)
MrHeat = Player('C150D09C-906C-4C53-8B6F-FDD752F883A9', 'Mr. Heat', NewEnglandMelee)
Nage = Player('D3B00EC5-2479-4E29-8FBE-32DEEFFD23D2', 'Nage', NewEnglandMelee)
Nico = Player('D4FE06C6-DA83-4CFF-957C-CBAC5C27D03C', 'Nico', NewEnglandMelee)
Nitro = Player('2678F735-C4C3-4182-8C1A-077C9F22F241', 'Nitro', NewEnglandMelee)
Ok = Player('D15F630E-9329-4430-B201-3D837A92EE25', 'Ok', NewEnglandMelee)
Omar = Player('E9CE59FB-4367-48F2-9A4B-14E8F6AD9064', 'Omar', NewEnglandMelee)
PERSI = Player('9A424A66-E8E4-402F-A22B-3A76A824C1E3', 'PERSI', NewEnglandMelee)
PeteyWalnuts = Player('2E5DBCD2-4D26-4E1F-B376-6F054FC5D06C', 'petey walnuts', NewEnglandMelee)
Pisces = Player('D97CF268-CA01-4ED3-92A4-01E11FF97284', 'Pisces', NewEnglandMelee)
PJ = Player('E42D8723-BEAA-45C8-AC52-ED47D5D77D3A', 'PJ', NewEnglandMelee)
Primer = Player('19B57F89-F85E-44A3-975A-6FC40B16154A', 'Primer', NewEnglandMelee)
Project = Player('55203EAD-758C-4892-96C4-6DF4600DC5F1', 'Project', NewEnglandMelee)
PSI = Player('3675716E-8E7E-427C-B98A-950150C5464F', 'PSI', NewEnglandMelee)
Q = Player('5C19CFD8-19CB-4F8A-A2DA-669928316A3E', 'Q', NewEnglandMelee)
RamZ = Player('862DB628-08CB-4EA9-AB56-D6CDDD24C82E', 'RamZ', NewEnglandMelee)
RatRattington = Player('FA73F3AA-3D89-4584-A3D3-3E44E4B61180', 'Rat Rattington', NewEnglandMelee)
Raventoly = Player('5CAAC238-1DB5-4D4D-8335-13872F21FE89', 'Raventoly', NewEnglandMelee)
RegEx = Player('1D8B9E33-86AE-45FB-89E9-0CB158C24FD3', 'regEx', NewEnglandMelee)
Riichi = Player('80D78051-C67C-4D23-880A-7203B12CDEBA', 'Riichi', NewEnglandMelee)
Ruby = Player('C8EB8852-704C-4748-97D2-C603B41FE697', 'Ruby', NewEnglandMelee)
RyGuy = Player('4BC14931-9607-475B-BA6B-8A04F6A39A2C', 'RyGuy', NewEnglandMelee)
RyuCloud = Player('6CB2416E-1A25-4F7D-B1BD-B2EFDEF6ED1C', 'RyuCloud', NewEnglandMelee)
Saturn = Player('E19282AB-6510-4560-A925-E84BBD995D23', 'Saturn', NewEnglandMelee)
Saucymain = Player('2407F41F-64A0-43AF-85F1-96F6985E57EE', 'saucymain', NewEnglandMelee)
Scooby = Player('0D6F7F6C-D586-40B6-8048-E141F00D6D36', 'Scooby', NewEnglandMelee)
Shmeeli = Player('39E544D6-60EC-4243-829E-C0E017FD58DC', 'Shmeeli', NewEnglandMelee)
Silver = Player('8C9E3D8E-7DD2-4A8A-B7F3-353AD81F1C19', 'Silver', NewEnglandMelee)
Slox = Player('C712C006-2C29-4CEF-8E66-0B3B47936142', 'Slox', NewEnglandMelee)
Snakefood = Player('693510EF-985E-4B4E-8EDC-E409EF087658', 'Snakefood', NewEnglandMelee)
Spades = Player('56BFF9EB-C155-4AEB-B717-F6024B4A36F5', 'Spades', NewEnglandMelee)
Speez = Player('5D28B44A-607E-48F2-8A58-50259254DCCE', 'Speez', NewEnglandMelee)
StacysStepdad = Player('EC16A4A0-715F-4675-8C89-C60E61BE85AE', 'Stacy\'s Stepdad', NewEnglandMelee)
Stickman = Player('5A44543D-559F-40E9-AB13-4011BCBF7FC0', 'Stickman', NewEnglandMelee)
Stus = Player('E752C4F4-33FB-48B9-9F75-FABB77CB9DC9', 'Stus', NewEnglandMelee)
Swampy = Player('FF959334-9EEC-4DF9-805D-4F088E71D92E', 'Swampy', NewEnglandMelee)
Sweat = Player('DF3CE0B4-0BA0-493F-99F3-879CD12469FD', 'Sweat', NewEnglandMelee)
Tarchwood = Player('1965DD31-F4D5-4BD1-B57C-D34B7657E12D', 'Tarchwood', NewEnglandMelee)
Tarkus = Player('96AEC556-D019-4323-980A-3EBCDECE1102', 'Tarkus', NewEnglandMelee)
Teakay = Player('7F2B8448-6F9B-4D12-B5C1-D80F168E0F11', 'Teakay', NewEnglandMelee)
Tenshi = Player('509509F0-DBF9-40A7-91E0-B2F5780B371F', 'Tenshi', NewEnglandMelee)
THEBEACHBOY = Player('99BDB145-CB14-4A9C-A23D-572BFCF470BD', 'THEBEACHBOY', NewEnglandMelee)
ThirtyThreeToes = Player('6F9C4639-E055-4F1E-845F-0741C9A053F2', '33 toes', NewEnglandMelee)
ThreeThreeThreeblobismOneOneOne = Player('8B56F081-A3B5-4A9A-8A74-16B673196433', '333blobism111', NewEnglandMelee)
ThroneButt = Player('ECE509E7-81DA-4C7A-81BC-D6D652C68785', 'ThroneButt', NewEnglandMelee)
Thumbs = Player('E4368902-0467-407D-98D2-D6220B066E6E', 'thumbs', NewEnglandMelee)
ThunderPaste = Player('E5452138-7949-4614-9F88-E30DC397357C', 'ThunderPaste', NewEnglandMelee)
Tommy = Player('A91E4B78-FA03-4747-BECB-4452298F1BEA', 'Tommy', NewEnglandMelee)
Trail = Player('6AAA1597-FEE6-4283-82E7-153A64997FA9', 'Trail', NewEnglandMelee)
TS420 = Player('F133BBB4-039D-40DB-BF64-8FCC84780423', 'TS420', NewEnglandMelee)
TwentyTwoK = Player('11CA20C1-5FDF-4A64-BC6C-0B5B91497FE7', '22K', NewEnglandMelee)
Twisty = Player('FF6DEEC7-30F3-4D9C-BD89-C44D0968033D', 'Twisty', NewEnglandMelee)
TwoCan = Player('99247341-865C-4056-8942-636C65BF0005', '2can', NewEnglandMelee)
Ubik = Player('6C4673F6-69D3-4D43-B585-DAF100BD2AE0', 'Ubik', NewEnglandMelee)
Veggietales = Player('7AA97FB5-6B21-4489-9823-EC3931625D3B', 'Veggietales', NewEnglandMelee)
Vinny = Player('39535E91-B2B7-4643-A966-C07179FA6546', 'Vinny', NewEnglandMelee)
Wang = Player('BCEF39FC-717A-4C0A-B806-F72DD38CBED3', 'wang', NewEnglandMelee)
WeWa = Player('81951490-D13C-4CE7-B0B9-CC130ADF73CF', 'WeWa', NewEnglandMelee)
Woodley = Player('315BD695-6105-4A53-92B4-5985F8F98A5F', 'Woodley', NewEnglandMelee)
Yami = Player('726A52BC-CF5A-4F17-A5EF-4604CC318F03', 'YAMI', NewEnglandMelee)
Yasu = Player('48AB25E0-1608-447B-B5A2-655AF6014E33', 'Yasu', NewEnglandMelee)
Versarchery = Player('5005FCDD-E1C5-4338-953B-B037688CE94D', 'versarchery', NewEnglandMelee)
Yifu = Player('856A527F-0BFA-4EF4-9D22-08950336DA47', 'Yifu', NewEnglandMelee)
Ymir = Player('7C7C8394-EFB5-4E3A-B137-9B96BA23FFEC', 'Ymir', NewEnglandMelee)
YoungCorgi = Player('20F78830-EF3F-4DF4-B348-EE940E764E27', 'Young Corgi', NewEnglandMelee)
Younger = Player('97D40D09-E9DF-468E-B90B-DD42CA8FA878', 'Younger', NewEnglandMelee)
YungHunn0 = Player('7FA52F7A-1A24-4F38-84A8-E43D312323AF', 'Yung Hunn0', NewEnglandMelee)
ZettaVolt = Player('39CC6481-F2DC-4D1D-8A51-AA4879873FEB', 'ZettaVolt', NewEnglandMelee)
Zoso = Player('879B158A-B151-4163-A530-8220A736AD9B', 'Zoso', NewEnglandMelee)
Zunk = Player('97B71974-9547-4894-97C4-47D9E0070059', 'Zunk', NewEnglandMelee)


# create WA players
Graves = Player('61E2DC0D-3795-40E6-87D3-A331AC9DE4CA', 'Graves',  WashingtonMelee)
Iceman = Player('B697375C-890A-4020-8868-CE66310BA1E3', 'Iceman', WashingtonMelee)
Vinodh = Player('9F2374B6-15FF-48BA-970A-34996F1CBC8A', 'Vinodh', WashingtonMelee)

NE_players = [Abel, Ac3r, AdmiralZhao, Alt, Alte, Analog, Ant, Arcade, Artelind, 
              Arty, AwesomeVideoGames, Bank, Bekvin, Ben, BLAK, Blizz, Bonfire10, 
              BonkCushy, Brub, Catfish, Clutch, Cocoa_, Conflict, Coolslice, Cupofwater, 
              Dad, Deadstock, Dour, DrLame, DrLobster, Dudutsai, Electroman, Ember, 
              Epoodle, ETHANBURKE, Eveningstar, Fats, FreeSSBM, Frosty, Fruity, 
              FutureShock, Glock, Glory, Golden, Greenstach, Guex, GWM420, Hexjo, 
              Hysteric, IOA, JNaut, Jwilli, Kacey, Kalvar, Keto, Khan, Kikoho, 
              Kota, KPeace, Kraft, Krakhead, Kuni, L33b, Lamdin, Lio, Loadspiller, 
              Louis, Makari, MEAT, Meep, Mike, MommyDaddy, MOOP, MrHeat, Nage, 
              Nico, Nitro, Ok, Omar, PERSI, PeteyWalnuts, Pisces, PJ, Primer, Project, 
              PSI, Q, RamZ, Raventoly, RegEx, Riichi, Ruby, RyGuy, RyuCloud, Saturn, 
              Saucymain, Scooby, Shmeeli, Silver, Slox, Snakefood, Spades, Speez, 
              StacysStepdad, Stickman, Stus, Swampy, Sweat, Tarchwood, Tarkus, 
              Teakay, Tenshi, THEBEACHBOY, ThirtyThreeToes, ThreeThreeThreeblobismOneOneOne, 
              ThroneButt, Thumbs, ThunderPaste, Trail, TS420, TwentyTwoK, Twisty, 
              TwoCan, Ubik, Veggietales, Vinny, Wang, WeWa, Woodley, Yami, Yasu, 
              Versarchery, Yifu, Ymir, YoungCorgi, Younger, YungHunn0, ZettaVolt, 
              Zoso, Zunk]