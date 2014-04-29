from nltk.corpus import wordnet as wn;

'''word = sys.argv[0];'''
word = 'dark';
print "WORD:\n" + word;
print;
synsets = wn.synsets(word);
#print "SYNSETS:"
if not synsets:
    print "Did not get synsets";
    exit(); #Fall back here
else:
    #print synsets;
    print "FIRST SENSE :\n" + synsets[0].name.split(".")[0];
############### HYPONYMS ###############
print "\nANTONYMS:"
lemmas = synsets[0].lemmas;
if not lemmas:
    print "Did not get lemmas"
else:
    #print "LEMMAS:\n" + str(synsets[0].lemmas[0]);
    antonyms = synsets[0].lemmas[0].antonyms();
    if not antonyms:
        print "Did not get antonyms"
    else:
        #print antonyms
        for antonym in antonyms:
            antonym = antonym.name.split(".")[0];
            print "Not "+ antonym +" but ....";
############### HYPONYMS ###############
print "\nHYPERNYMS:"
hypernyms = synsets[0].hypernyms()
if not hypernyms:
    print "Did not get hyponyms";
else:
    #print hypernyms;
    for hypernym in hypernyms:
        hypernym = hypernym.name.split(".")[0];
        print "It is a type of " + hypernym;
############### HYPERNYMS ###############
print "\nHYPONYMS:"
hyponyms = synsets[0].hyponyms()
if not hyponyms:
    print "Did not get hyponyms";
else:
    #print hyponyms;
    for hyponym in hyponyms:
        hyponym = hyponym.name.split(".")[0];
        print "It is like a " + hyponym;
