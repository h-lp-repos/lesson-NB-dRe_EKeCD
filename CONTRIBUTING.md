# Contributing and Submission Guidelines

Thank you for working on Assignment P2! Please follow these steps to prepare your submission:

1. **Fork & Clone**
   - Fork this repository to your GitHub account.
   - Clone your fork locally:
     ```bash
     git clone https://github.com/your-username/lesson-NB-dRe_EKeCD.git
     ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/<your-name>-p2
   ```

3. **Implement**
   - Complete the pipeline steps in `src/build_index.py` and `src/query.py`.
   - Ensure `data/faq_document.txt` has enough content.
   - Update `outputs/sample_queries.json` with your sample runs.

4. **Run Tests**
   ```bash
   ./scripts/run_tests.sh
   ```

5. **Commit & Push**
   ```bash
   git add .
   git commit -m "Add <your-name> solutions for Assignment P2"
   git push origin feature/<your-name>-p2
   ```

6. **Submit a Pull Request**
   - Open a PR against the `main` branch of the original repo.
   - Include a clear description of your implementation choices.

7. **Review & Feedback**
   - Address any review comments.

Good luck and happy coding!
