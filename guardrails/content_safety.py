"""
Content Safety Checker
RUBRIC: Governance & Guardrails - Content safety checks (2 marks)

TASK: Implement keyword-based content safety checking
"""

import logging
from typing import Dict, List

logger = logging.getLogger(__name__)

class ContentSafety:
    """Checks content for safety violations"""
    
    def __init__(self):
        # HINT: Define unsafe keyword patterns for different categories
        self.unsafe_patterns = {
            'violence': [],  # HINT: List of violence-related keywords like ['kill', 'attack', etc.]
            'hate_speech': [],  # HINT: List of hate speech keywords like
            'profanity': [],  # HINT: List of profanity keywords
            'personal_attack': []  # HINT: List of personal attack keywords like
        }
        
        # HINT: Define travel-specific red flags
        self.travel_red_flags = []  # HINT: List like ['fraud', 'fake booking', 'scam', etc.]
    
    def check(self, text: str) -> Dict:
        """
        Check text for safety violations
        
        HINT: This method should:
        1. Convert text to lowercase
        2. Initialize empty flags list
        3. Check text against unsafe_patterns
        4. Check text against travel_red_flags
        5. Return dict with is_safe, flags, severity
        """
        text_lower = text.lower()  # HINT: .lower()
        flags = []
        
        # HINT: Check general unsafe patterns
        for category, keywords in self.unsafe_patterns.items(): 
            for keyword in keywords:
                if keyword in text_lower:  
                    flags.append({
                        'category': category,
                        'keyword': keyword,   
                        'severity': 'high' # HINT: 'high' for violence/hate speech, 'medium' for profanity, 'low' for personal attack
                    })
        
        # HINT: Check travel-specific red flags
        for red_flag in self.travel_red_flags: 
            if red_flag in text_lower:
                flags.append({
                    'category': 'travel_red_flag', 
                    'keyword': red_flag,  
                    'severity': 'high' 
                })
        
        return {
            'is_safe': len(flags) == 0, 
            'flags': flags,    
            'severity': 'high' if any(f['severity'] == 'high' for f in flags) else ('medium' if any(f['severity'] == 'medium' for f in flags) else 'low') if flags else 'none'  
        }
    
    def get_safety_score(self, text: str) -> float:
        """
        Calculate safety score (0-1)
        
        HINT: Return 1.0 if safe, otherwise reduce by 0.2 per flag (minimum 0.0)
        """
        result = self.check(text) 
        
        if result['is_safe']:  
            return 1.0 
        
        # HINT: Reduce score based on violations
        penalty = 0.2 * len(result['flags'])  
        return max(0.0, 1.0 - penalty) 