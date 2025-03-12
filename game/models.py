from django.db import models

class GameResult(models.Model):
    DIFFICULTY_CHOICES = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    )
    player_name = models.CharField(max_length=100, blank=True, default="Anonymous")
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='Easy')
    correct_count = models.IntegerField(default=0)
    wrong_count = models.IntegerField(default=0)
    total_attempts = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player_name} - {self.difficulty} ({self.correct_count} correct)"
