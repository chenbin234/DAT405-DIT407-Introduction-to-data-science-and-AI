import os


hamtest = ['easy_ham/0733.782a236e90e0e7a55b3c67be6f7bef23', 'easy_ham/0006.ee8b0dba12856155222be180ba122058', 'easy_ham/1420.6954e3e5e7c772dc859c47d42ff4a085', 'easy_ham/1979.3e2071d1c381de05d3395a56623f39d7', 'easy_ham/0274.62155dd02f8719d2cfd0f76671549737', 'easy_ham/0650.98f5c18e05ccd24028b10fa7317d67e8', 'easy_ham/1987.c891203fbc1f19431e30d96928aec430', 'easy_ham/0575.2f6d5a053932e0900b329a15c5f78e38']

messages = []
for file in hamtest:
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        messages.append((content, "ham" if "ham" in hamtest else "spam"))


# messages = []
# with open('spam/0174.3874b6ff3c86a5ebefb558138a6bfb28', 'r', encoding='utf-8', errors='ignore') as f:
#     content = f.read()
#     messages.append(
#         (content, "spam" if "spam" in 'spam/0174.3874b6ff3c86a5ebefb558138a6bfb28' else "ham"))

print(messages)

