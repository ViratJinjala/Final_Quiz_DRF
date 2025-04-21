-- Clear existing data (optional, uncomment if needed)
-- DELETE FROM users_question;
-- DELETE FROM users_quiz;
-- DELETE FROM users_chapter;
-- DELETE FROM users_subject;

-- Insert Subjects
INSERT INTO users_subject (name, description) VALUES
('Mathematics', 'Fundamental concepts of mathematics including algebra, calculus, and statistics'),
('Physics', 'Study of matter, energy, and their interactions'),
('Chemistry', 'Study of substances, their properties, and transformations'),
('Biology', 'Study of living organisms and their interactions'),
('Computer Science', 'Study of computers, computing, and computational systems');

-- Insert Chapters
INSERT INTO users_chapter (subject_id, name, description) VALUES
-- Mathematics Chapters
(1, 'Algebra', 'Study of mathematical symbols and rules for manipulating them'),
(1, 'Calculus', 'Study of continuous change and motion'),
(1, 'Statistics', 'Study of data collection, analysis, and interpretation'),

-- Physics Chapters
(2, 'Mechanics', 'Study of motion and forces'),
(2, 'Thermodynamics', 'Study of heat and energy'),
(2, 'Electromagnetism', 'Study of electric and magnetic fields'),

-- Chemistry Chapters
(3, 'Organic Chemistry', 'Study of carbon compounds'),
(3, 'Inorganic Chemistry', 'Study of non-carbon compounds'),
(3, 'Physical Chemistry', 'Study of chemical processes'),

-- Biology Chapters
(4, 'Cell Biology', 'Study of cell structure and function'),
(4, 'Genetics', 'Study of genes and heredity'),
(4, 'Ecology', 'Study of organisms and their environment'),

-- Computer Science Chapters
(5, 'Programming', 'Study of computer programming and algorithms'),
(5, 'Data Structures', 'Study of organizing and storing data'),
(5, 'Networks', 'Study of computer networks and communication');

-- Insert Quizzes
INSERT INTO users_quiz (chapter_id, date_of_quiz, time_duration, remarks) VALUES
-- Mathematics - Algebra
(1, '2024-04-25', '30 minutes', 'Basic algebraic concepts'),
(1, '2024-04-26', '45 minutes', 'Advanced algebraic concepts'),

-- Mathematics - Calculus
(2, '2024-04-25', '30 minutes', 'Basic calculus concepts'),
(2, '2024-04-26', '45 minutes', 'Advanced calculus concepts'),

-- Mathematics - Statistics
(3, '2024-04-25', '30 minutes', 'Basic statistics concepts'),
(3, '2024-04-26', '45 minutes', 'Advanced statistics concepts'),

-- Physics - Mechanics
(4, '2024-04-25', '30 minutes', 'Basic mechanics concepts'),
(4, '2024-04-26', '45 minutes', 'Advanced mechanics concepts'),

-- Physics - Thermodynamics
(5, '2024-04-25', '30 minutes', 'Basic thermodynamics concepts'),
(5, '2024-04-26', '45 minutes', 'Advanced thermodynamics concepts'),

-- Physics - Electromagnetism
(6, '2024-04-25', '30 minutes', 'Basic electromagnetism concepts'),
(6, '2024-04-26', '45 minutes', 'Advanced electromagnetism concepts'),

-- Chemistry - Organic Chemistry
(7, '2024-04-25', '30 minutes', 'Basic organic chemistry concepts'),
(7, '2024-04-26', '45 minutes', 'Advanced organic chemistry concepts'),

-- Chemistry - Inorganic Chemistry
(8, '2024-04-25', '30 minutes', 'Basic inorganic chemistry concepts'),
(8, '2024-04-26', '45 minutes', 'Advanced inorganic chemistry concepts'),

-- Chemistry - Physical Chemistry
(9, '2024-04-25', '30 minutes', 'Basic physical chemistry concepts'),
(9, '2024-04-26', '45 minutes', 'Advanced physical chemistry concepts'),

-- Biology - Cell Biology
(10, '2024-04-25', '30 minutes', 'Basic cell biology concepts'),
(10, '2024-04-26', '45 minutes', 'Advanced cell biology concepts'),

-- Biology - Genetics
(11, '2024-04-25', '30 minutes', 'Basic genetics concepts'),
(11, '2024-04-26', '45 minutes', 'Advanced genetics concepts'),

-- Biology - Ecology
(12, '2024-04-25', '30 minutes', 'Basic ecology concepts'),
(12, '2024-04-26', '45 minutes', 'Advanced ecology concepts'),

-- Computer Science - Programming
(13, '2024-04-25', '30 minutes', 'Basic programming concepts'),
(13, '2024-04-26', '45 minutes', 'Advanced programming concepts'),

-- Computer Science - Data Structures
(14, '2024-04-25', '30 minutes', 'Basic data structures concepts'),
(14, '2024-04-26', '45 minutes', 'Advanced data structures concepts'),

-- Computer Science - Networks
(15, '2024-04-25', '30 minutes', 'Basic networks concepts'),
(15, '2024-04-26', '45 minutes', 'Advanced networks concepts');

-- Insert Questions
INSERT INTO users_question (quiz_id, question_statement, option1, option2, option3, option4, correct_option, weightage) VALUES
-- Mathematics - Algebra Basic (Quiz 1)
(1, 'What is the value of x in the equation 2x + 5 = 15?', '5', '7', '10', '15', 2, 1),
(1, 'Simplify: (x + 2)(x - 2)', 'x² - 4', 'x² + 4', 'x² - 2', 'x² + 2', 1, 1),
(1, 'Solve for x: 3x - 7 = 14', '5', '7', '8', '9', 2, 1),
(1, 'What is the slope of the line y = 2x + 3?', '2', '3', '5', '6', 1, 1),
(1, 'Factor: x² - 9', '(x+3)(x-3)', '(x+9)(x-9)', '(x+1)(x-9)', '(x+3)(x+3)', 1, 1),
(1, 'Solve: 4x + 8 = 20', '3', '4', '5', '6', 1, 1),
(1, 'What is the y-intercept of y = -2x + 5?', '-2', '0', '5', '7', 3, 1),
(1, 'Simplify: 2(x + 3) + 3(x - 1)', '5x + 3', '5x + 6', '5x + 9', '5x + 12', 1, 1),
(1, 'Solve: x² = 16', '±4', '±8', '±16', '±32', 1, 1),
(1, 'What is the domain of f(x) = √(x-2)?', 'x ≥ 2', 'x > 2', 'x ≤ 2', 'x < 2', 1, 1),

-- Mathematics - Algebra Advanced (Quiz 2)
(2, 'Solve the quadratic equation: x² + 5x + 6 = 0', 'x = -2, -3', 'x = -1, -6', 'x = 2, 3', 'x = 1, 6', 1, 2),
(2, 'What is the vertex of the parabola y = x² + 4x + 3?', '(-2, -1)', '(-2, 1)', '(2, -1)', '(2, 1)', 1, 2),
(2, 'Simplify: (x + h)² - x²', '2xh + h²', '2x + h', 'x² + h²', '2x² + h', 1, 2),
(2, 'Solve the system: 2x + y = 5, 3x - y = 1', 'x = 2, y = 1', 'x = 1, y = 3', 'x = 3, y = -1', 'x = 4, y = -3', 1, 2),
(2, 'What is the range of f(x) = x² + 1?', 'y ≥ 1', 'y > 1', 'y ≤ 1', 'y < 1', 1, 2),
(2, 'Factor: x³ - 8', '(x-2)(x²+2x+4)', '(x+2)(x²-2x+4)', '(x-2)(x²-2x+4)', '(x+2)(x²+2x+4)', 1, 2),
(2, 'Solve: log₂(x) = 3', '8', '6', '9', '7', 1, 2),
(2, 'What is the inverse of f(x) = 2x + 3?', '(x-3)/2', '(x+3)/2', '2x-3', '-2x+3', 1, 2),
(2, 'Simplify: (x² - 4)/(x + 2)', 'x - 2', 'x + 2', 'x² - 2', 'x² + 2', 1, 2),
(2, 'Solve: |x - 3| = 5', 'x = -2, 8', 'x = -5, 5', 'x = -8, 2', 'x = -3, 3', 1, 2),

-- Physics - Mechanics Basic (Quiz 4)
(4, 'What is Newton''s First Law?', 'Law of Inertia', 'Law of Acceleration', 'Law of Action-Reaction', 'Law of Gravity', 1, 1),
(4, 'What is the SI unit of force?', 'Newton', 'Joule', 'Pascal', 'Watt', 1, 1),
(4, 'What is acceleration?', 'Rate of change of velocity', 'Rate of change of position', 'Rate of change of force', 'Rate of change of mass', 1, 1),
(4, 'What is the formula for kinetic energy?', '½mv²', 'mv', 'mgh', 'F=ma', 1, 1),
(4, 'What is the unit of work?', 'Joule', 'Newton', 'Watt', 'Pascal', 1, 1),
(4, 'What is momentum?', 'Mass × Velocity', 'Force × Distance', 'Mass × Acceleration', 'Force × Time', 1, 1),
(4, 'What is the unit of power?', 'Watt', 'Joule', 'Newton', 'Pascal', 1, 1),
(4, 'What is the formula for potential energy?', 'mgh', '½mv²', 'F=ma', 'p=mv', 1, 1),
(4, 'What is friction?', 'Force opposing motion', 'Force causing motion', 'Force of gravity', 'Force of magnetism', 1, 1),
(4, 'What is the unit of mass?', 'Kilogram', 'Newton', 'Joule', 'Watt', 1, 1),

-- Chemistry - Organic Chemistry Basic (Quiz 7)
(7, 'What is the general formula for alkanes?', 'CnH2n+2', 'CnH2n', 'CnH2n-2', 'CnH2n-4', 1, 1),
(7, 'What is a functional group?', 'Group of atoms giving characteristic properties', 'Group of molecules', 'Group of compounds', 'Group of elements', 1, 1),
(7, 'What is the IUPAC name for CH3CH2OH?', 'Ethanol', 'Methanol', 'Propanol', 'Butanol', 1, 1),
(7, 'What is an isomer?', 'Same formula, different structure', 'Different formula, same structure', 'Same formula and structure', 'Different formula and structure', 1, 1),
(7, 'What is the general formula for alkenes?', 'CnH2n', 'CnH2n+2', 'CnH2n-2', 'CnH2n-4', 1, 1),
(7, 'What is a hydrocarbon?', 'Compound of carbon and hydrogen', 'Compound of carbon and oxygen', 'Compound of carbon and nitrogen', 'Compound of carbon and sulfur', 1, 1),
(7, 'What is the general formula for alkynes?', 'CnH2n-2', 'CnH2n', 'CnH2n+2', 'CnH2n-4', 1, 1),
(7, 'What is a polymer?', 'Long chain of repeating units', 'Short chain of different units', 'Mixture of compounds', 'Single compound', 1, 1),
(7, 'What is the functional group of alcohols?', '-OH', '-COOH', '-NH2', '-CHO', 1, 1),
(7, 'What is the general formula for carboxylic acids?', 'R-COOH', 'R-OH', 'R-NH2', 'R-CHO', 1, 1),

-- Computer Science - Programming Basic (Quiz 13)
(13, 'What is a variable?', 'Storage location with a name', 'Mathematical equation', 'Computer program', 'Data type', 1, 1),
(13, 'What is a loop?', 'Repeated execution of code', 'Single execution of code', 'Code termination', 'Code compilation', 1, 1),
(13, 'What is an array?', 'Collection of similar elements', 'Single element', 'Mathematical function', 'Computer hardware', 1, 1),
(13, 'What is a function?', 'Reusable block of code', 'Variable declaration', 'Data type', 'Loop structure', 1, 1),
(13, 'What is debugging?', 'Finding and fixing errors', 'Writing code', 'Compiling code', 'Running code', 1, 1),
(13, 'What is an algorithm?', 'Step-by-step solution', 'Computer program', 'Programming language', 'Data structure', 1, 1),
(13, 'What is a compiler?', 'Translates code to machine language', 'Executes code', 'Writes code', 'Debugs code', 1, 1),
(13, 'What is a string?', 'Sequence of characters', 'Number', 'Boolean value', 'Array', 1, 1),
(13, 'What is recursion?', 'Function calling itself', 'Loop structure', 'Variable declaration', 'Data type', 1, 1),
(13, 'What is object-oriented programming?', 'Programming using objects', 'Linear programming', 'Functional programming', 'Procedural programming', 1, 1);

-- Add more questions for remaining quizzes following the same pattern... 