from experta import *
import requests


class cooking(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.current_question = ""
        self.started = False
        self.fact_name = ""
        self.end = False
        self.suggestion = ""
        
    def send_question(self,question,fact_name):
        self.current_question = question
        self.fact_name = fact_name
        # Make an API request to send the question
        requests.post('http://localhost:5000/ask_question',json={'question': question})
    
    def send_suggestion(self,suggestion):
        self.end = True
        self.suggestion = suggestion
        requests.post('http://localhost:5000/get_suggestion', json={'suggestion': suggestion})
        
    
    @Rule(NOT(Fact(n=W())))
    def ask(self):
        self.send_question("what is your budget for a trip between? answers:100K-200k,200k-300k",fact_name='n')
    @Rule(AND(NOT(Fact(g=W())),Fact(n="100k-200k")))
    def ask1(self):
        self.send_question("what do you prefer? answers:maritime climate, mountain climate, other",fact_name='g')
    @Rule(AND(NOT(Fact(l=W())),Fact(g="maritime climate")))
    def ask2(self):
        self.send_question("do you prefer? answers:secluded beach, public beach",fact_name='l')
    @Rule(AND(Fact(l="secluded beach"),Fact(g="maritime climate")))
    def printxham474583847384933492(self):
        self.send_suggestion("Al-Samra Beach: This is a secluded beach located in the north of Syria.It is known for its clear waters and its golden sand. There are no facilities at the beach, so it is a popular destination for those who want to relax and enjoy the peace and quiet.  Wadi Qandil Beach: This is a secluded beach located in the mountains of Syria. It is known for its clear waters and its stunning scenery. There are no facilities at the beach, so it is a popular destination for those who want to go hiking and camping.  Ras al-Naqurah Beach: This is a secluded beach located in the south of Syria. It is known for its clear waters and its beautiful coral reefs. There are no facilities at the beach, so it is a popular destination for snorkeling and diving enthusiasts.")
    @Rule(AND(Fact(l="public beach"),Fact(g="maritime climate")))
    def printxhamfe(self):
        self.send_suggestion("Bilbil Beach: This beach is located in the city of Latakia and is a popular spot for locals. It is a long, sandy beach with clear blue waters. There are no facilities on the beach, but it is a great place to relax and swim. El Menzel Beach: This beach is located in the city of Jableh and is known for its calm waters. It is a popular spot for families and couples. There are a few restaurants and cafes on the beach, but no other facilities. Arwad Island Beaches: This island is located off the coast of Tartous and is a popular spot for day trips. There are several beaches on the island, all of which are public. The waters are clear and calm, and the beaches are sandy.")   
    @Rule(AND(NOT(Fact(l=W())),Fact(g="mountain climate")))
    def ask243(self):
        self.send_question("do you prefer? answers:fold mounatins, Block mountains, Dome mountains",fact_name='l')
    @Rule(AND(Fact(l="fold mounatins"),Fact(g="mountain climate")))
    def printxham9403(self):
        self.send_suggestion("Al-Jabal al-Aqra: This is the highest mountain in Syria, located in the western part of the country. It is a fold mountain that was formed by the collision of the Arabian and African plates. The mountain is home to a number of hiking trails and viewpoints, and it offers stunning views of the surrounding countryside.  Al-Jabal al-Sawda: This is a mountain range located in the southern part of Syria. It is a fold mountain that was formed by the collision of the Arabian and African plates. The mountain range is home to a number of hiking trails and monasteries, and it offers stunning views of the surrounding desert")
    @Rule(AND(Fact(l="Block mountains"),Fact(g="mountain climate")))
    def printxham205844904(self):
        self.send_suggestion("Jebel Druze: This is a mountain range located in the south of Syria. It is a block mountain that was formed by the uplift of a fault block. The mountain range is home to a number of Druze villages, and it offers stunning views of the surrounding desert.  Jebel Bishri: This is a mountain range located in the central part of Syria. It is a block mountain that was formed by the uplift of a fault block. The mountain range is home to a number of ancient ruins, and it offers stunning views of the surrounding countryside.")
    @Rule(AND(Fact(l="Dome mountains"),Fact(g="mountain climate")))
    def printxham47458492(self):
        self.send_suggestion("Qalamun Mountains: These are a group of mountains located in the western part of Syria. They are dome mountains that were formed by the uplift of a magma chamber. The mountains are home to a number of forests and springs, and they offer stunning views of the surrounding countryside. Jebel Zawiya: This is a mountain located in the north of Syria. It is a dome mountain that was formed by the uplift of a magma chamber. The mountain is home to a number of hiking trails and monasteries, and it offers stunning views of the surrounding countryside")
    @Rule(AND(NOT(Fact(l=W())),Fact(g="other")))
    def ask2420346740(self):
        self.send_question("what are you interested in? answers:nature trips, historical trips",fact_name = 'l')
    @Rule(AND(NOT(Fact(k=W())),Fact(g="other"),Fact(l="nature trips")))
    def ask246340548(self):
        self.send_question("what kind of nature activities are you interested in? answers:hiking, camping, rafting, wildlife watching",fact_name='k')
    @Rule(AND(NOT(Fact(f=W())),Fact(k="hiking"),Fact(g="other"),Fact(l="nature trips")))
    def ask240634059(self):
        self.send_question("are you looking for a challenging hike with? answers:stunning views, more leisurely stroll through the woods",fact_name='f')
    @Rule(AND(NOT(Fact(j=W())),Fact(f="challenging hike with stunning views"),Fact(k="hiking"),Fact(g="other"),Fact(l="nature trips")))
    def ask2461757653(self):
        self.send_question("you prefer hiking in? answers:long distance or short distance",fact_name='j')
    @Rule(AND(Fact(j="long distance"),Fact(f="challenging hike with stunning views"),Fact(k="hiking"),Fact(l="nature trips"),Fact(g="other")))
    def printxham9324455456(self):
        self.send_suggestion("Al-Ghab Plain: Situated in the western part of Syria, this vast plain is known for its greenery and picturesque landscapes. You can hike through the fields and enjoy the serene beauty of nature.")
    @Rule(AND(Fact(j="short distance"),Fact(f="challenging hike with stunning views"),Fact(k="hiking"),Fact(l="nature trips"),Fact(g="other")))
    def printxham93546575445(self):
        self.send_suggestion("Mount Qassioun: Located near Damascus, this mountain offers stunning views of the city and the surrounding landscapes. It's a popular spot for short hikes and picnics, and the trails are easily accessible.,Dead Cities: These ancient abandoned cities, such as Serjilla and Al-Bara, are located in northwestern Syria and offer unique hiking experiences. You can explore the ruins and enjoy the scenic beauty of the countryside.,Crac des Chevaliers: This medieval castle near Homs not only has historical significance but also offers breathtaking views from its hilltop location. You can hike up to the castle and enjoy the panoramic vistas.")
    @Rule(AND(NOT(Fact(j=W())),Fact(f="more leisurely stroll through the woods"),Fact(k="hiking"),Fact(g="other"),Fact(l="nature trips")))
    def ask246133344505(self):
        self.send_question("you prefer hiking in? answers:long distance or short distance",fact_name='j')
    @Rule(AND(Fact(j="long distance"),Fact(f="more leisurely stroll through the woods"),Fact(k="hiking"),Fact(l="nature trips"),Fact(g="other")))
    def printxham9935942(self):
        self.send_suggestion("Hawran Forests: Located in the southern region, the Hawran Forests offer extensive trails through lush greenery and diverse wildlife. Al-Zabadani Forest: Situated near Al-Zabadani, this forest provides a picturesque setting with trails winding through dense trees. Al-Nuri Forest Reserve:Located in the Aleppo countryside, the Al-Nuri Forest Reserve features oak and pine trees, with trails meandering through beautiful landscape")
    @Rule(AND(Fact(j="short distance"),Fact(f="more leisurely stroll through the woods"),Fact(k="hiking"),Fact(l="nature trips"),Fact(g="other")))
    def printxham933488760(self):
        self.send_suggestion("Forests of Latakia: The coastal province of Latakia offers small forests, such as Wadi Qandil and Wadi Deir Hanna, with picturesque wooded trails suitable for leisurely hikes.")
    @Rule(AND(NOT(Fact(f=W())),Fact(k="camping"),Fact(g="other"),Fact(l="nature trips")))
    def ask24069090909485653(self):
        self.send_question("are you looking for camping for? answers:outdoor enthusiasts, indoor camping(glamorous camping)",fact_name='f')
    @Rule(AND(NOT(Fact(j=W())),Fact(f="outdoor enthusiasts"),Fact(k="camping"),Fact(g="other"),Fact(l="nature trips")))
    def ask246175049645545487(self):
        self.send_question("you prefer? answers:wilderness camping, beach camping",fact_name='j')
    @Rule(AND(Fact(j="wilderness camping"),Fact(f="outdoor enthusiasts"),Fact(k="camping"),Fact(l="nature trips"),Fact(g="other")))
    def printxham93229484554544456(self):
        self.send_suggestion("Al-Razaza Lake: Located in the desert region of eastern Syria, Al-Razaza Lake offers a unique wilderness camping experience. You can set up your tent near the lake and enjoy the serene desert surroundings. Al-Ghab Plain: Situated in the western part of Syria, Al-Ghab Plain is a vast open space perfect for wilderness camping. You can pitch your tent amidst the green fields and enjoy the tranquility of nature. Mount Hermon: This mountain in southwestern Syria offers opportunities for wilderness camping. You can camp in the higher altitudes, surrounded by stunning landscapes and fresh mountain air.")
    @Rule(AND(Fact(j="beach camping"),Fact(f="outdoor enthusiasts"),Fact(k="camping"),Fact(l="nature trips"),Fact(g="other")))
    def printxham932456fh354549(self):
        self.send_suggestion("Latakia Beach: The coastal city of Latakia offers beautiful beaches where you can set up your tent and enjoy beach camping. You can swim in the Mediterranean Sea and relax by the shore. Tartus Beach: Located on the Mediterranean coast, Tartus has picturesque beaches ideal for camping. You can enjoy the sound of the waves and the stunning sunsets while camping by the beach. Jableh Beach: Another coastal town with lovely beaches, Jableh provides camping spots where you can enjoy the sea breeze and the sandy shores.")
    @Rule(AND(NOT(Fact(j=W())),Fact(f="indoor camping(glamorous camping)"),Fact(k="camping"),Fact(g="other"),Fact(l="nature trips")))
    def ask2461754545837(self):
        self.send_question("you prefer? answers:camping pods, glamping tents",fact_name='j')
    @Rule(AND(Fact(j="camping pods"),Fact(f="indoor camping(glamorous camping)"),Fact(k="camping"),Fact(l="nature trips"),Fact(g="other")))
    def printxham93245jf4796(self):
        self.send_suggestion("Latakia Camping Pods: Along the coast of Latakia, you can find camping pods that provide a unique indoor camping experience. These pods offer comfortable sleeping arrangements, basic amenities, and a cost-effective option for glamping. You can enjoy the beach and other nearby attractions during the day and retreat to your cozy pod in the evening.")
    @Rule(AND(Fact(j="glamping tents"),Fact(f="indoor camping(glamorous camping)"),Fact(k="camping"),Fact(l="nature trips"),Fact(g="other")))
    def printxham93245id9457756(self):
        self.send_suggestion("Tartus Glamping Tents: In the coastal city of Tartus, you can find glamping tents that offer a comfortable and affordable camping experience. These tents are equipped with cozy beds, furnishings, and basic amenities.")
    @Rule(AND(NOT(Fact(f=W())),Fact(k="wildlife watching"),Fact(g="other"),Fact(l="nature trips")))
    def ask2400865467665753(self):
        self.send_question("where do you prefer watching wildlife in? answers:various nature habitats such as lakes, forests?",fact_name='f')
    @Rule(AND(Fact(f="lakes"),Fact(k="wildlife watching"),Fact(l="nature trips"),Fact(g="other")))
    def printxham9322948443346645544436(self):
        self.send_suggestion("Al-Razaza Lake: Located in the eastern desert region of Syria, Al-Razaza Lake is known for its rich birdlife. You can observe various migratory birds and waterfowl in their natural habitat.")
    @Rule(AND(Fact(f="forests"),Fact(k="wildlife watching"),Fact(l="nature trips"),Fact(g="other")))
    def printxham9322938484445653098765456(self):
        self.send_suggestion("Barada River Valley: Situated near Damascus, the Barada River Valley is home to diverse wildlife species. You can spot birds, small mammals, and reptiles while enjoying a leisurely stroll through the forests")
    @Rule(AND(NOT(Fact(k=W())),Fact(g="other"),Fact(l="historical trips")))
    def ask243578749876444623393(self):
        self.send_question("what kind of historical sites are you interested in? answers:Museums, castles",fact_name='k')
    @Rule(AND(NOT(Fact(f=W())),Fact(k="Museums"),Fact(g="other"),Fact(l="historical trips")))
    def ask2406434565456458765645893(self):
        self.send_question("which types of museum do you prefer? answers:archaeology museums, history museums",fact_name='f')
    @Rule(AND(NOT(Fact(j=W())),Fact(f="archaeology museums"),Fact(k="Museums"),Fact(g="other"),Fact(l="historical trips")))
    def ask2461768765449545843493(self):
        self.send_question("do you want more informations about archaeology museums? answers:yes,no",fact_name='j')
    @Rule(AND(Fact(j="yes"),Fact(f="archaeology museums"),Fact(k="Museums"),Fact(l="historical trips"),Fact(g="other")))
    def printxham944554324984358355396(self):
        self.send_suggestion(" Archaeology museums in Syria display artifacts and objects related to the country's rich archaeological heritage. They often showcase ancient ruins, sculptures, pottery, and other archaeological finds. and those are the places: National Museum of Damascus: Located in Damascus, this museum houses a vast collection of archaeological artifacts from various periods of Syria's history. You can explore exhibits showcasing ancient civilizations, including the Bronze Age, Roman, and Byzantine eras.  Aleppo Museum: Situated in the city of Aleppo, this museum offers a rich display of archaeological finds from the region. You can admire artifacts from different historical periods, including the Hittite, Assyrian, and Islamic civilizations.")
    @Rule(AND(Fact(j="no"),Fact(f="archaeology museums"),Fact(k="Museums"),Fact(l="historical trips"),Fact(g="other")))
    def printxham9445543248940539356(self):
        self.send_suggestion("National Museum of Damascus: Located in Damascus, this museum houses a vast collection of archaeological artifacts from various periods of Syria's history. You can explore exhibits showcasing ancient civilizations, including the Bronze Age, Roman, and Byzantine eras.  Aleppo Museum: Situated in the city of Aleppo, this museum offers a rich display of archaeological finds from the region. You can admire artifacts from different historical periods, including the Hittite, Assyrian, and Islamic civilizations.")
    @Rule(AND(NOT(Fact(j=W())),Fact(f="history museums"),Fact(k="Museums"),Fact(g="other"),Fact(l="historical trips")))
    def ask24617688776544954536556(self):
        self.send_question("do you want more informations about archaeology museums? answers:yes,no",fact_name='j')
    @Rule(AND(Fact(j="yes"),Fact(f="history museums"),Fact(k="Museums"),Fact(l="historical trips"),Fact(g="other")))
    def printxham944554893294435449096(self):
        self.send_suggestion("These museums focus on different periods of Syrian history and display historical artifacts, documents, and multimedia exhibits to educate visitors about the country's past. and  those are the places:  Hama Museum: Located in the city of Hama, this museum showcases the history and culture of the region. You can learn about the city's ancient past, including its role in the Roman and Islamic periods. Raqqa Museum: Situated in the city of Raqqa, this museum provides insights into the history and heritage of the region. You can explore exhibits highlighting the city's significance during the Abbasid and Ayyubid dynasties")
    @Rule(AND(Fact(j="no"),Fact(f="history museums"),Fact(k="Museums"),Fact(l="historical trips"),Fact(g="other")))
    def printxham944554903244767898548356(self):
        self.send_suggestion(" Hama Museum: Located in the city of Hama, this museum showcases the history and culture of the region. You can learn about the city's ancient past, including its role in the Roman and Islamic periods. Raqqa Museum: Situated in the city of Raqqa, this museum provides insights into the history and heritage of the region. You can explore exhibits highlighting the city's significance during the Abbasid and Ayyubid dynasties")
    @Rule(AND(NOT(Fact(f=W())),Fact(k="castles"),Fact(g="other"),Fact(l="historical trips")))
    def ask24064345654564588499685993(self):
        self.send_question("which types of castles do you prefer? answers:desert forts, Hisotrical castles",fact_name='f')
    @Rule(AND(NOT(Fact(j=W())),Fact(f="Hisotrical castles"),Fact(k="castles"),Fact(g="other"),Fact(l="historical trips")))
    def ask246176887765449506789906767849453(self):
        self.send_question("do you want more informations about Hisotrical castles? answers:yes,no",fact_name='j')
    @Rule(AND(Fact(j="yes"),Fact(f="Hisotrical castles"),Fact(k="castles"),Fact(l="historical trips"),Fact(g="other")))
    def printxham94455489329899443584956(self):
        self.send_suggestion("Historical castles in Syria are significant landmarks that showcase the rich cultural and historical heritage of the region .and also those are the places  Krak des Alawites: Located near the town of Masyaf, Krak des Alawites is a historical castle that dates back to the 11th century. It served as a stronghold for the Nizari Ismaili sect during the Crusader era. While not as well-known as some other castles in Syria, it offers a unique glimpse into the region's history and provides panoramic views of the surrounding landscape.")
    @Rule(AND(Fact(j="no"),Fact(f="Hisotrical castles"),Fact(k="castles"),Fact(l="historical trips"),Fact(g="other")))
    def printxham944554903244767835456489096(self):
        self.send_suggestion(" Krak des Alawites: Located near the town of Masyaf, Krak des Alawites is a historical castle that dates back to the 11th century. It served as a stronghold for the Nizari Ismaili sect during the Crusader era. While not as well-known as some other castles in Syria, it offers a unique glimpse into the region's history and provides panoramic views of the surrounding landscape.")
    @Rule(AND(NOT(Fact(j=W())),Fact(f="desert forts"),Fact(k="castles"),Fact(g="other"),Fact(l="historical trips")))
    def ask246176887765449905584945569843(self):
        self.send_question("do you want more informations about desert forts? answers:yes,no",fact_name='j')
    @Rule(AND(Fact(j="yes"),Fact(f="desert forts"),Fact(k="castles"),Fact(l="historical trips"),Fact(g="other")))
    def printxham94455489329099549484948844356(self):
        self.send_suggestion("Syria has several desert forts that were constructed to protect trade routes and settlements in the desert regions. These forts were typically made of mud or stone and provided defense against nomadic raids. and also those are the places Qasr al-Hayr al-Gharbi: Located in the Syrian Desert, Qasr al-Hayr al-Gharbi is a fortified palace that served as a caravanserai during the Islamic period. It showcases the architectural grandeur of the desert forts and offers a unique experience. You can explore the palace and admire the desert surroundings.")
    @Rule(AND(Fact(j="no"),Fact(f="desert forts"),Fact(k="castles"),Fact(l="historical trips"),Fact(g="other")))
    def printxham9445543244769044595978883956(self):
        self.send_suggestion("Qasr al-Hayr al-Gharbi: Located in the Syrian Desert, Qasr al-Hayr al-Gharbi is a fortified palace that served as a caravanserai during the Islamic period. It showcases the architectural grandeur of the desert forts and offers a unique experience. You can explore the palace and admire the desert surroundings.")
    @Rule(AND(NOT(Fact(g=W())),Fact(n="200k-300k")))
    def ask13484(self):
        self.send_question("what do you prefer? answers:maritime climate, mountain climate, other",fact_name='g')
    @Rule(AND(NOT(Fact(l=W())),Fact(g="maritime climate")))
    def ask893454452(self):
        self.send_question("do you prefer? answers:secluded beach, private beach",fact_name='l')
    @Rule(AND(Fact(l="secluded beach"),Fact(g="maritime climate")))
    def printxham47473374583847384933492(self):
        self.send_suggestion("1. Ras al-Basit: Located near Latakia, Ras al-Basit is known for its pristine beaches and rocky coastline. Exploring this area may lead you to discover secluded coves and hidden beaches.  2. Arwad Island: Situated off the coast of Tartus, Arwad Island is the only inhabited island in Syria. It offers a unique and tranquil atmosphere, and you may find secluded spots along its shores.  3. Kadmous Beach: This beach is located near Banias, a city in the Tartus Governorate. While it can get crowded during peak tourist seasons, there are sections of the beach that are less frequented and offer a more secluded experience.")
    @Rule(AND(Fact(l="private beach"),Fact(g="maritime climate")))
    def printxha54598mfe(self):
        self.send_suggestion("1. Coral Beach Hotel & Resort (Latakia): This luxury hotel is situated on a private beach in Latakia and offers exclusive beach access for its guests. 2. Blue Beach Resort (Tartus): Located in Tartus, this beachfront resort may have a private beach area for its guests to enjoy. 3. San Stephano Resort (Latakia): Situated in Latakia, this resort boasts a private beach where guests can relax and soak up the sun. 4.Afamia Rotana Resort (Latakia): This resort in Latakia is known for its beautiful beachfront location and may offer private beach access for its guests.")   
    @Rule(AND(NOT(Fact(l=W())),Fact(g="mountain climate")))
    def ask2988643(self):
        self.send_question("do you prefer? answers:fold mounatins, Block mountains, Dome mountains",fact_name='l')
    @Rule(AND(Fact(l="fold mounatins"),Fact(g="mountain climate")))
    def printxham944848403(self):
        self.send_suggestion("Jebel Qamishli: This is a fold mountain located in the northeastern part of Syria, about 200 kilometers (120 miles) from the nearest conflict zone. It is 1,604 meters (5,261 ft) tall and is a popular destination for hiking, camping, and bird watching. They are fold mountains. Jebel Kurd Dagh: This is a fold mountain located in the northeastern part of Syria, about 150 kilometers (93 miles) from the nearest conflict zone. It is 1,259 meters (4,128 ft) tall and is a popular destination for hiking and rock climbing.")
    @Rule(AND(Fact(l="Block mountains"),Fact(g="mountain climate")))
    def printxham2058445567904(self):
        self.send_suggestion("Jebel el-Khadhir: This is a block mountain located in the central part of Syria, about 100 kilometers (62 miles) from the nearest conflict zone. It is 1,383 meters (4,537 ft) tall and is a popular destination for hiking and camping.")
    @Rule(AND(Fact(l="Dome mountains"),Fact(g="mountain climate")))
    def printxham4745849044482(self):
        self.send_suggestion("Jebel Zawiyeh: This is a dome mountain located in the southwestern part of Syria, about 150 kilometers (93 miles) from the nearest conflict zone. It is 1,120 meters (3,674 ft) tall and is a popular destination for hiking and exploring the ruins of ancient villages. Qalat Salamiyah: This is a dome mountain located in the central part of Syria, about 150 kilometers (93 miles) from the nearest conflict zone. It is 1,150 meters (3,773 ft) tall and is a popular destination for hiking and exploring the ruins of a medieval castle.")
    @Rule(AND(NOT(Fact(l=W())),Fact(g="other")))
    def ask2420346494830740(self):
        self.send_question("are you interested in? answers:nature trips, historical trips",fact_name='l')
    @Rule(AND(NOT(Fact(k=W())),Fact(g="other"),Fact(l="nature trips")))
    def ask2463405494348(self):
        self.send_question("what kind of nature activities are you interested in? answers:hiking, camping, rafting, wildlife watching",fact_name='k')
    @Rule(AND(NOT(Fact(f=W())),Fact(k="hiking"),Fact(g="other"),Fact(l="nature trips")))
    def ask2406340540489(self):
        self.send_question("are you looking for a challenging hike with? answers:stunning views, more leisurely stroll through the woods",fact_name='f')
    @Rule(AND(NOT(Fact(j=W())),Fact(f="challenging hike with stunning views"),Fact(k="hiking"),Fact(g="other"),Fact(l="nature trips")))
    def ask246175764444953(self):
        self.send_question("you prefer hiking in? answers:long distance or short distance",fact_name='j')
    @Rule(AND(Fact(j="long distance"),Fact(f="challenging hike with stunning views"),Fact(k="hiking"),Fact(l="nature trips"),Fact(g="other")))
    def printxham9324955040455456(self):
        self.send_suggestion("Mount Hermon: Located in southwestern Syria, Mount Hermon is the highest peak in the country. Hiking to its summit offers breathtaking panoramic views of the surrounding landscape. Crac des Chevaliers to Qalaat Salah El-Din: This long-distance hike takes you through ancient ruins, including the majestic Crusader fortress known as Crac des Chevaliers. The trail leads to Qalaat Salah El-Din, another picturesque fortification perched atop a hill.")
    @Rule(AND(Fact(j="short distance"),Fact(f="challenging hike with stunning views"),Fact(k="hiking"),Fact(l="nature trips"),Fact(g="other")))
    def printxham93545436575445(self):
        self.send_suggestion("Dead Cities of Serjilla and Al Bara: These UNESCO World Heritage sites are easily accessible for a short hike. The ruins of Serjilla and Al Bara provide a fascinating glimpse into ancient civilizations, with unique architectural structures set against a backdrop of rural countryside. Palmyra: Located in the Syrian Desert, the ancient city of Palmyra (Tadmur) offers shorter hiking routes that allow you to explore its impressive archaeological ruins, including the monumental Roman theatre and the Temple of Bel.")
    @Rule(AND(NOT(Fact(j=W())),Fact(f="more leisurely stroll through the woods"),Fact(k="hiking"),Fact(g="other"),Fact(l="nature trips")))
    def ask24613334455443300705(self):
        self.send_question("you prefer hiking in? answers:long distance or short distance",fact_name='j')
    @Rule(AND(Fact(j="long distance"),Fact(f="more leisurely stroll through the woods"),Fact(k="hiking"),Fact(l="nature trips"),Fact(g="other")))
    def printxham993843939295942(self):
        self.send_suggestion("1.Al-Hosein Forest: Located near the city of Latakia, Al-Hosein Forest offers a long-distance hiking trail through lush woodlands. The trail is surrounded by beautiful flora and fauna, making it a great choice for nature enthusiasts seeking a challenging hike.  2. Al-Midan Forest: Situated near Tartus, Al-Midan Forest provides a scenic long-distance hiking option. With its dense vegetation and peaceful ambiance, this trail offers a delightful escape into the woods.")
    @Rule(AND(Fact(j="short distance"),Fact(f="more leisurely stroll through the woods"),Fact(k="hiking"),Fact(l="nature trips"),Fact(g="other")))
    def printxham933433939339393988760(self):
        self.send_suggestion("1. Al-Salaliyah Forest: For a shorter, leisurely hike through the woods, Al-Salaliyah Forest in Hama is an excellent choice. The trail offers a serene atmosphere, perfect for a relaxing walk surrounded by nature. 2. Al-Jazaa Forest: Located near Aleppo, Al-Jazaa Forest offers a picturesque short-distance hiking trail through enchanting woodlands. It's an ideal option for those looking to enjoy a calm and refreshing walk in nature.")
    @Rule(AND(NOT(Fact(f=W())),Fact(k="camping"),Fact(g="other"),Fact(l="nature trips")))
    def ask2406909090948448484485653(self):
        self.send_question("are you looking for camping for? answers:outdoor enthusiasts, indoor camping(glamorous camping)",fact_name='j')
    @Rule(AND(NOT(Fact(j=W())),Fact(f="outdoor enthusiasts"),Fact(k="camping"),Fact(g="other"),Fact(l="nature trips")))
    def ask246175049648383375545487(self):
        self.send_question("you prefer? answers:Desert Camping, Caravan Camping, Cultural Camping",fact_name='j')
    @Rule(AND(Fact(j="Desert Camping"),Fact(f="outdoor enthusiasts"),Fact(k="camping"),Fact(l="nature trips"),Fact(g="other")))
    def printxham9322933733748489889554544456(self):
        self.send_suggestion("1. Palmyra Desert: The ancient city of Palmyra in the eastern part of Syria offers desert camping opportunities. You can set up camp in the desert and experience the vastness and beauty of the Syrian deserts. 2. Deir ez-Zor Desert: This region in eastern Syria has expansive desert landscapes where you can camp and immerse yourself in the desert atmosphere. Professional guides and proper equipment are recommended for this type of camping.")
    @Rule(AND(Fact(j="Caravan Camping"),Fact(f="outdoor enthusiasts"),Fact(k="camping"),Fact(l="nature trips"),Fact(g="other")))
    def printxham9324520248482392296fh354549(self):
        self.send_suggestion("1. Aleppo Citadel: The historic city of Aleppo offers caravan camping opportunities near its famous citadel. You can park your caravan and explore the city's cultural heritage while enjoying the convenience of your own accommodation. 2. Krak des Chevaliers: This medieval castle near Homs has camping facilities for caravans. You can stay overnight and explore the castle and its surroundings at your leisure.")
    @Rule(AND(Fact(j="Cultural Camping"),Fact(f="outdoor enthusiasts"),Fact(k="camping"),Fact(l="nature trips"),Fact(g="other")))
    def printxham9324520227899392296fh354549(self):
        self.send_suggestion("Palmyra: Camping near the ancient ruins of Palmyra allows you to experience the cultural heritage of Syria up close. Enjoy the unique blend of history and nature while camping in the vicinity of this UNESCO World Heritage site.")
    @Rule(AND(NOT(Fact(j=W())),Fact(f="indoor camping(glamorous camping)"),Fact(k="camping"),Fact(g="other"),Fact(l="nature trips")))
    def ask24617545458933822737(self):
        self.send_question("you prefer? answers:Luxury Tented Camps, Mountain Cabins ",fact_name='j')
    @Rule(AND(Fact(j="Luxury Tented Camps"),Fact(f="indoor camping(glamorous camping)"),Fact(k="camping"),Fact(l="nature trips"),Fact(g="other")))
    def printxham93245jf43838228796(self):
        self.send_suggestion("1. Palmyra Luxury Tented Camp: Located near the ancient ruins of Palmyra, this camp offers luxurious tented accommodations with comfortable beds, private bathrooms, and upscale amenities. You can enjoy the beauty of the desert while experiencing the comforts of a high-end camp. 2. Aleppo Luxury Tented Camp: Situated near the historic city of Aleppo, this luxury tented camp provides a glamorous camping experience with spacious tents, luxurious furnishings, and personalized services. You can explore the city's cultural attractions during the day and retreat to your lavish tent in the evening.")
    @Rule(AND(Fact(j="Mountain Cabins"),Fact(f="indoor camping(glamorous camping)"),Fact(k="camping"),Fact(l="nature trips"),Fact(g="other")))
    def printxham93245id94573338339756(self):
        self.send_suggestion("Qalamoun Mountain Cabins: In the scenic Qalamoun Mountains, you can find mountain cabins that offer a cozy and luxurious camping experience. These cabins provide comfortable beds, modern amenities, and stunning views of the surrounding mountains. You can enjoy hiking and other outdoor activities during the day and relax in the comfort of your cabin at night.")
    @Rule(AND(NOT(Fact(f=W())),Fact(k="wildlife watching"),Fact(g="other"),Fact(l="nature trips")))
    def ask24008654683383387665753(self):
        self.send_question("where do you prefer watching wildlife in? answers:various nature habitats such as Mountains, National Park ?",fact_name='f')
    @Rule(AND(Fact(f="Mountains"),Fact(k="wildlife watching"),Fact(l="nature trips"),Fact(g="other")))
    def printxham932294844334638438338645544436(self):
        self.send_suggestion(" Jebel Ansariyah: Located in the coastal region of Syria, Jebel Ansariyah offers opportunities to spot wildlife such as mountain goats, foxes, and various bird species. You can hike through the mountains and enjoy the breathtaking views while observing the local fauna.")
    @Rule(AND(Fact(f="National Park"),Fact(k="wildlife watching"),Fact(l="nature trips"),Fact(g="other")))
    def printxham932293848444538338383653098765456(self):
        self.send_suggestion("Al Talila National Park: Located in the eastern part of Syria, Al Talila National Park is a protected area that offers a variety of wildlife-watching opportunities. You can spot species like the Arabian oryx, gazelles, and different bird species. It is recommended to hire a local guide for a better wildlife-watching experience.")
    @Rule(AND(NOT(Fact(k=W())),Fact(g="other"),Fact(l="historical trips")))
    def ask24357874987644462338333943093(self):
        self.send_question("what kind of historical sites are you interested in? answers:Museums, castles",fact_name='k')
    @Rule(AND(NOT(Fact(f=W())),Fact(k="Museums"),Fact(g="other"),Fact(l="historical trips")))
    def ask2406434565456458765630933845893(self):
        self.send_question("which types of museum do you prefer? answers:Art museums, Cultural museums",fact_name='f')
    @Rule(AND(NOT(Fact(j=W())),Fact(f="Art museums"),Fact(k="Museums"),Fact(g="other"),Fact(l="historical trips")))
    def ask24617687654495458439339320493(self):
        self.send_question("do you want more informations about Art museums? answers:yes,no",fact_name='j')
    @Rule(AND(Fact(j="yes"),Fact(f="Art museums"),Fact(k="Museums"),Fact(l="historical trips"),Fact(g="other")))
    def printxham9445543249843583553393022096(self):
        self.send_suggestion("Syria is home to several art museums that exhibit both traditional and contemporary artworks. These museums showcase paintings, sculptures, ceramics, and other forms of artistic expression by Syrian and international artists. so those are places for art museums: 1. Damascus National Museum of Modern Art: Located in Damascus, this museum focuses on modern and contemporary Syrian art. You can admire works by renowned Syrian artists and gain insights into the country's vibrant art scene. 2. Aleppo Art Gallery: Situated in Aleppo, this art gallery showcases a diverse collection of contemporary artworks by Syrian artists. You can explore various mediums and styles, reflecting the artistic talent of the region.")
    @Rule(AND(Fact(j="no"),Fact(f="Art museums"),Fact(k="Museums"),Fact(l="historical trips"),Fact(g="other")))
    def printxham9445543248940538393939356(self):
        self.send_suggestion("1. Damascus National Museum of Modern Art: Located in Damascus, this museum focuses on modern and contemporary Syrian art. You can admire works by renowned Syrian artists and gain insights into the country's vibrant art scene. 2. Aleppo Art Gallery: Situated in Aleppo, this art gallery showcases a diverse collection of contemporary artworks by Syrian artists. You can explore various mediums and styles, reflecting the artistic talent of the region.")
    @Rule(AND(NOT(Fact(j=W())),Fact(f="Cultural museums"),Fact(k="Museums"),Fact(g="other"),Fact(l="historical trips")))
    def ask2461768877654495457383393936556(self):
        self.send_question("do you want more informations about Cultural museums? answers:yes,no",fact_name='j')
    @Rule(AND(Fact(j="yes"),Fact(f="Cultural museums"),Fact(k="Museums"),Fact(l="historical trips"),Fact(g="other")))
    def printxham9445548932944354494345678096(self):
        self.send_suggestion("Cultural museums in Syria aim to preserve and promote the diverse cultural heritage of the country. They often display traditional costumes, handicrafts, musical instruments, and other cultural artifacts. These museums provide insights into the customs, traditions, and lifestyles of different communities in Syria,  so those are places for Cultural museums: 1. Aleppo Citadel Museum: Housed within the historic Aleppo Citadel, this museum offers exhibits on the cultural history of the region. You can learn about the architectural heritage, traditional crafts, and cultural practices of Aleppo. 2. Maarat al-Numan Museum: Located in the town of Maarat al-Numan, this museum focuses on the cultural heritage and history of the region. You can explore displays on traditional crafts, folk traditions, and local customs.")
    @Rule(AND(Fact(j="no"),Fact(f="Cultural museums"),Fact(k="Museums"),Fact(l="historical trips"),Fact(g="other")))
    def printxham94455490324476789854856344453356(self):
        self.send_suggestion("1. Aleppo Citadel Museum: Housed within the historic Aleppo Citadel, this museum offers exhibits on the cultural history of the region. You can learn about the architectural heritage, traditional crafts, and cultural practices of Aleppo. 2. Maarat al-Numan Museum: Located in the town of Maarat al-Numan, this museum focuses on the cultural heritage and history of the region. You can explore displays on traditional crafts, folk traditions, and local customs.")
    @Rule(AND(NOT(Fact(f=W())),Fact(k="castles"),Fact(g="other"),Fact(l="historical trips")))
    def ask24064345654564588495678549685993(self):
        self.send_question("which types of castles do you prefer? answers:Crusader castles, Islamic castles",fact_name='f')
    @Rule(AND(NOT(Fact(j=W())),Fact(f="Crusader castles"),Fact(k="castles"),Fact(g="other"),Fact(l="historical trips")))
    def ask2461768877654495067893456789765906767849453(self):
        self.send_question("do you want more informations about Crusader castles? answers:yes,no",fact_name='j')
    @Rule(AND(Fact(j="yes"),Fact(f="Crusader castles"),Fact(k="castles"),Fact(l="historical trips"),Fact(g="other")))
    def printxham9445548932989944747884356433584956(self):
        self.send_suggestion("Crusader castles were built by European Crusaders during the medieval period. These castles served as military fortresses and were strategically located along important trade routes. those are places for  Crusader castles: 1. Crac des Chevaliers: Located near the town of Homs, Crac des Chevaliers is one of the most iconic and well-preserved Crusader castles in the world. It offers a fascinating glimpse into the medieval Crusader period and showcases impressive architecture and defensive features.")
    @Rule(AND(Fact(j="no"),Fact(f="Crusader castles"),Fact(k="castles"),Fact(l="historical trips"),Fact(g="other")))
    def printxham9445549032447678355673456489096(self):
        self.send_suggestion("1. Crac des Chevaliers: Located near the town of Homs, Crac des Chevaliers is one of the most iconic and well-preserved Crusader castles in the world. It offers a fascinating glimpse into the medieval Crusader period and showcases impressive architecture and defensive features.")
    @Rule(AND(NOT(Fact(j=W())),Fact(f="Islamic castles"),Fact(k="castles"),Fact(g="other"),Fact(l="historical trips")))
    def ask2461768877654499055849455545446769843(self):
        self.send_question("do you want more informations about Islamic castles? answers:yes,no",fact_name='j')
    @Rule(AND(Fact(j="yes"),Fact(f="Islamic castles"),Fact(k="castles"),Fact(l="historical trips"),Fact(g="other")))
    def printxham944554893290995494567756584948844356(self):
        self.send_suggestion("Islamic citadels, also known as qal'at, were fortified structures built during the Islamic period. These citadels served as military fortresses and administrative centers. those are places about islamic castles: 1. Citadel of Aleppo: Situated in the city of Aleppo, the Citadel is a historic fortress that dates back to ancient times. It played a significant role in Islamic history and offers a fascinating glimpse into the region's Islamic heritage. You can explore the castle grounds and visit the Aleppo Citadel Museum, which displays artifacts from various periods.")
    @Rule(AND(Fact(j="no"),Fact(f="Islamic castles"),Fact(k="castles"),Fact(l="historical trips"),Fact(g="other")))
    def printxham9445543244769044595978883449458548956(self):
        self.send_suggestion("1. Citadel of Aleppo: Situated in the city of Aleppo, the Citadel is a historic fortress that dates back to ancient times. It played a significant role in Islamic history and offers a fascinating glimpse into the region's Islamic heritage. You can explore the castle grounds and visit the Aleppo Citadel Museum, which displays artifacts from various periods.")