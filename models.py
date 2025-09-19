from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Example model: QuantumCommand
class QuantumCommand(db.Model):
    __tablename__ = 'quantum_commands'
    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.String(255), nullable=False)
    similarity_score = db.Column(db.Float)

    def __repr__(self):
        return f"<QuantumCommand {self.command}>"
