from nltk.corpus import wordnet as wn;

'''word = sys.argv[0];'''
word = 'floss';
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
for synset in synsets: 
    lemmas = synset.lemmas;
    if lemmas:
        #print "LEMMAS:\n" + str(synsets[0].lemmas[0]);
        for lemma in synset.lemmas:
            antonyms = lemma.antonyms();
            if antonyms:
                #print antonyms
                for antonym in antonyms:
                    sAntonym = antonym.name.split(".")[0];
                    print "Not "+ sAntonym +" but ...."; 
############### HYPONYMS ###############
print "\nHYPERNYMS:"
for synset in synsets: 
    hypernyms = synset.hypernyms()
    if hypernyms:
        #print hypernyms;
        for hypernym in hypernyms:
            sHypernym = hypernym.name.split(".")[0];
            print "It is a type of " + sHypernym;
            if hypernym.examples:
                print  "as in ";
                print "'" + hypernym.examples[0]+ "'";
############### HYPERNYMS ###############
print "\nHYPONYMS:"
for synset in synsets: 
    hyponyms = synset.hyponyms()
    if hyponyms:
        #print hyponyms;
        for hyponym in hyponyms:
            sHyponym = hyponym.name.split(".")[0];
            print "It is like " + sHyponym;
            if hyponym.examples:
                print "as in "
                print "'" + hyponym.examples[0]+ "'";
