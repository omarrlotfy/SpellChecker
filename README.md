# SpellChecker
This project implements a spell checker class in Python that efficiently handles a given dictionary using a suitable data structure. The spell checker class offers three main operations to ensure accurate and fast spell checking functionalities

*Store the Dictionary:
The spell checker class takes the input dictionary and stores it in a highly efficient data structure. By choosing the appropriate data structure, the spell checker ensures fast retrieval and searching capabilities. Commonly used data structures like hash tables or trie are employed to achieve an average-case time complexity of O(N), where N is the number of words in the dictionary. Additionally, the space complexity for storing the dictionary is O(N), ensuring efficient memory utilization.

*Find Nearest 4 Words:
When given an input word that is not present in the dictionary, the spell checker swiftly identifies the nearest four words in lexicographic order. Efficient search algorithms, such as binary search, are utilized to achieve a time complexity of O(log N), where N is the number of words in the dictionary. The nearest four words are returned without additional data structures, ensuring a space complexity of O(1).

*Add Word to the Dictionary:
The spell checker class allows users to add new words to the dictionary, ensuring its adaptability and flexibility. The addition operation is optimized for speed and memory usage. For hash tables, the average-case time complexity for word insertion is O(1), while for trie, it is O(K), where K is the length of the word. The space complexity for adding a word is minimal, ensuring efficient use of memory resources.

Overall, this spell checker class offers a robust and efficient solution for spell checking tasks. With its smart data structure choice, it ensures fast spell checking, accurate word suggestions for unknown words, and seamless addition of new words to the dictionary. Whether used in text processing, writing applications, or data analysis, this spell checker class is designed to deliver top-notch performance and user-friendly functionality.

Please note: The nearest four words from a word are defined as the two words before and after the given word in lexicographic order if they exist. This spell checker class is suitable for use in various applications where reliable spell checking and word suggestion functionalities are required.
