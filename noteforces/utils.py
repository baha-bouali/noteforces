def format_note(note):
    """Format note tuple into readable string."""
    id, tag, rating, ideas, time_spent, editorial, created_at = note
    return f"[{id}] {tag} | {rating} | {ideas} | {time_spent}min | Editorial: {editorial} | {created_at}"
