import unittest
from app.models import Pitch, User, Comment
from app import db

class TestPitch(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(pitch_content = "pitch one", pitch_category='Business')
        self.new_comment = Comment(comment_content = "One comment", pitch=self.new_pitch)
    
    def tearDown(self):
        db.session.delete(self)
        User.query.commit()
        

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment_content,"One comment")
        self.assertEquals(self.new_comment.pitch,self.new_pitch, 'pitch one')
