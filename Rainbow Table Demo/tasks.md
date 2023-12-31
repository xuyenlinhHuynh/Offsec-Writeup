# Rainbow Table Attack: Beginner Tasks

Hashing algorithm used in this project: `springroll_hashing` made by me :3 See the algorithm (function) in task 4 folder.

Task 1. I am Jon the hacker. I found a start-up company having lack of security in their system. So, I broke into their system and stole their database detail. But... the password seems already being hashed. Can you help me crack these hashes (find the plaintext password) ?

    - Files: `database.txt` -- the actual database from the company.
             `passwd_only_db.txt` -- containing only users' passwords.
             `springroll_hashing_table.txt` -- the pre-computed hash table using the `springroll_hashing` algorithm.

Task 2. Again I am Jon the hacker. I have been offered a position as a penetration tester in the same company that I hacked before. I have signed up a staff account. But... something went wrong? I cannot sign in the staff portal using the registered account!! So, I hack into the system again to check if I have been registered into the database. I found there were 4 users having the same username as me! Can you check if I am one of the `Jon` in the database? My plaintext password is `Jon123`.

    - Files: `output.txt` -- Part of the database showing user(s) `Jon`.
             `passwd_only_db.txt` -- The hashes of `Jon`.
             `springroll_hashing_table.txt` -- the pre-computed hash table using the `springroll_hashing` algorithm.

Task 3. Hey, I am Jon again. I failed to crack the following hash: `9e9f7d6b9992` using rainbow table attack. Can you tell me some potential reasons why I failed in this case?

    - Files: `secret_hash.txt` -- The hash of the password.
             `springroll_hashing_table.txt` -- the pre-computed hash table using the `springroll_hashing` algorithm.

Task 4. Suppose the password in this company has to start with `Jon`. I found the `springroll_hashing` algorithm and I think this is not a good hashing algorithm... It means that I can turn this `hashing` algorithm to a normal `encryption` algorithm, and develop a `decryption` algorithm to break it. Can you help me to write one and solve the hash in `secret_hash.txt` ? 

    - Files: `secret_hash.txt` -- The hash of the password.
             `springroll_hashing.py` -- The hashing algorithm.

Task 5. Wait... If I can `decrypt` the ciphertext, then I think I can break the password given on Task 3 and login as admin!!!! Can you help me to crack it?

    - Files: `secret_hash.txt` -- The hash of the password.
             `springroll_hashing.py` -- The hashing algorithm.
             `login.c` -- The login page (To run this, following these steps: gcc login.c --> ./a.out [password]). 
             Note that if you wish, you can crack the password by playing around with binary ;) (reverse engineering).

ADDITIONAL FILES:
- `springroll_lookup.sh`: Purpose -- to match the given hash to a plaintext password in the rainbow table; if not found, it will print out "Not Found". Format -- bash file. Usage -- ./springroll_lookup.sh \[hash\]. Note -- when running the file, make sure it is in the same folder/repository/directory as the rainbow table (hash table).

 