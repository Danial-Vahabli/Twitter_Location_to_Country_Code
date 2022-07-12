The Algorithm maps the “location string” of a twitter user to its country using dictionaries. The output of the function is the Alpha-2 country codes. A full list of codes is available under:
https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
Database:

We use 3 seperate dictionaries to map the locations:
1)	Country_Names_dict: Original Name of the countries and their alpha 2 code.
2)	Original_Names_dict: Original Name of Locations and their alpha 2 code. (Resource: GeoNames, https://www.geonames.org/)
3)	Alternative_Names_exp: Alternative Name of Locations and their alpha 2 code. (Resource: GeoNames, https://www.geonames.org/)
Algorithm:
The algorithm first checks whether the string has any alphabetical charachter or not. If not, the functions outputs “Error”, then it splits the string using “,” and “ “ and then tries to find matches going through database from 1 to 3.  If there is no match at this stage, the algorithm checks whether the string contains the alpha 2 code or not. finally, if there is not a match yet, the algorithm checks the alphabet that the charachters belong, if they are Cyrillic, the output is Russia and if they are CJK characters the output is Japan. Finally, if the function does not find a match, it will export Error.

Outputs:
1)	Alpha 2 codes
2)	“Error”: This either menas that the string doesnt correposnd to an actual location like “she/Her”, “Hell” or a fictional location like “Hogwarts”. It is also possible that the function could not find any match for the location while it is refering to an actual location. The latter is rare.

Accuracy:

To check the accuracy, we have a list of 815 most frequent twitter locations which are manually labelled. (Most_Frequent_Locations_Labelled.csv) using this file, we have checked the accuracy and weighted accuracy while going down on the list.

Accuracy: Number of Correct Results/Total Results

Weighted Accuracy: Sum of the frequency of correct results/total frequency

The results are as follows for “ALL” of the dataset and few countries:
               


![ALL](https://user-images.githubusercontent.com/107769994/178612336-3d47866c-ba62-40dd-83b9-2f25b7712f2f.png)


![US](https://user-images.githubusercontent.com/107769994/178612354-7839b43c-1a30-49f4-bcb5-2f43eb733198.png)


![JP](https://user-images.githubusercontent.com/107769994/178612369-69dc9397-17ba-4a94-8b30-ecdbc768e3db.png)


![RU](https://user-images.githubusercontent.com/107769994/178612384-ceb0c40a-2b1b-48d9-bf0d-9ba5292ccadb.png)

![BR](https://user-images.githubusercontent.com/107769994/178612412-3d463d8f-d8ea-4160-8367-6542a36eca31.png)

![AR](https://user-images.githubusercontent.com/107769994/178612421-1979335d-43cd-477c-90fb-1263cb7f7c86.png)

![GB](https://user-images.githubusercontent.com/107769994/178612428-18cd2e5c-d261-43ed-81cf-77dbb661b96b.png)

![IN](https://user-images.githubusercontent.com/107769994/178612479-599fb74e-f301-403c-9ae1-3fccf69eecbe.png)












