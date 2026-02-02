from flask import Blueprint, request, jsonify
from app.models import db, Student

# Step 1: Create a Blueprint

# Blueprints allow us to organize routes modularly.
# This blueprint handles all student-related routes.

student_bp = Blueprint('student', __name__)

# Step 2: POST /students → Add a new student

@student_bp.route('', methods=['POST'])
def add_student():
    """
    Create a new student record in the database.
    Expects JSON body with: name, domain, gpa, email
    """
    data = request.get_json()

    # Validate required fields
    if not data or not all(key in data for key in ('name', 'domain', 'gpa', 'email')):
        return jsonify({"error": "Missing data"}), 400

    # Create a new Student instance
    new_student = Student(
        name=data['name'],
        domain=data['domain'],
        gpa=data['gpa'],
        email=data['email']
    )
    
    # Add and commit to the database
    db.session.add(new_student)
    db.session.commit()
    
    return jsonify({"message": "Student added successfully!", "id": new_student.id}), 201

# Step 3: GET /students → Retrieve all students

@student_bp.route('', methods=['GET'])
def get_students():
    """
    Return a list of all students in the database.
    """
    students = Student.query.all()  # Fetch all student records

    # Convert SQLAlchemy objects to JSON
    student_list = [
        {
            "id": student.id,
            "name": student.name,
            "domain": student.domain,
            "gpa": student.gpa,
            "email": student.email
        } for student in students
    ]
    
    return jsonify(student_list), 200

# Step 4: GET /students/<id> → Retrieve a single student

@student_bp.route('<int:student_id>', methods=['GET'])
def get_student(student_id):
    """
    Fetch a single student by ID.
    Returns 404 if not found.
    """
    student = Student.query.get_or_404(student_id)  # Get student or return 404
    
    return jsonify({
        "id": student.id,
        "name": student.name,
        "domain": student.domain,
        "gpa": student.gpa,
        "email": student.email
    }), 200

# Step 5: PUT /students/<id> → Update a student

@student_bp.route('<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """
    Update fields of an existing student.
    Only updates fields provided in the JSON body.
    """
    student = Student.query.get_or_404(student_id)  # Fetch student or 404
    data = request.get_json()

    # Validate at least one valid field is provided
    if not data or not any(key in data for key in ('name', 'domain', 'gpa', 'email')):
        return jsonify({"error": "No valid fields provided"}), 400

    # Update the fields if present
    if 'name' in data:
        student.name = data['name']
    if 'domain' in data:
        student.domain = data['domain']
    if 'gpa' in data:
        student.gpa = data['gpa']
    if 'email' in data:
        student.email = data['email']
    
    # Commit changes to the database
    db.session.commit()
    
    return jsonify({"message": "Student updated successfully!"}), 200

# Step 6: DELETE /students/<id> → Delete a student

@student_bp.route('<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """
    Delete a student record by ID.
    Returns 404 if student not found.
    """
    student = Student.query.get_or_404(student_id)  # Fetch student or 404
    
    # Delete and commit
    db.session.delete(student)
    db.session.commit()
    
    return jsonify({"message": "Student deleted successfully!"}), 200
