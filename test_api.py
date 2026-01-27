import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
BASE_URL = "http://localhost:8000"

def test_basic_questions():
    """Test basic questions without conversation history"""
    print("\n" + "="*60)
    print("TEST 1: Basic Questions (No History)")
    print("="*60 + "\n")
    
    test_prompts = [
        "How should I live my life?",
    ]
    
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    successful_responses = 0
    
    for prompt in test_prompts:
        try:
            print(f"❓ Question: {prompt}")
            print("-" * 60)
            
            response = requests.get(
                f"{BASE_URL}/api",
                params={"input": prompt},
                headers=headers,
                timeout=30
            )
            
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            data = response.json()
            answer = data.get('response', '')
            assert answer, "No response received"
            
            print(f"✅ Response:\n{answer}\n")
            successful_responses += 1
            
        except AssertionError as e:
            print(f"❌ Assertion Error: {e}\n")
        except requests.exceptions.ConnectionError:
            print(f"❌ Connection Error: Cannot connect to {BASE_URL}\n")
            raise
        except Exception as e:
            print(f"❌ Error: {e}\n")
    
    print("="*60)
    print(f"✅ Basic Questions Test: {successful_responses}/{len(test_prompts)} passed\n")
    assert successful_responses == len(test_prompts), f"Only {successful_responses}/{len(test_prompts)} tests passed"


def test_conversation_history():
    """Test multi-turn conversation with history"""
    print("\n" + "="*60)
    print("TEST 2: Multi-Turn Conversation (With History)")
    print("="*60 + "\n")
    
    conversation = []
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    
    # First question
    q1 = "What is virtue?"
    print(f"❓ Question 1: {q1}")
    print("-" * 60)
    
    try:
        response = requests.get(
            f"{BASE_URL}/api",
            params={"input": q1},
            headers=headers,
            timeout=30
        )
        
        assert response.status_code == 200, f"Q1: Expected 200, got {response.status_code}"
        data = response.json()
        answer1 = data.get('response', '')
        assert answer1, "Q1: No response received"
        
        print(f"✅ Response:\n{answer1}\n")
        
        conversation.append({"role": "user", "content": q1})
        conversation.append({"role": "assistant", "content": str(answer1)})
        
    except AssertionError as e:
        print(f"❌ Assertion Error: {e}\n")
        raise
    except Exception as e:
        print(f"❌ Error: {e}\n")
        raise
    
    print("="*60 + "\n")
    
    # Second question (with history)
    q2 = "Based on what you just said, how do I practice virtue in my daily life?"
    print(f"❓ Question 2: {q2}")
    print(f"📝 Conversation History: {len(conversation)} messages")
    print("-" * 60)
    
    try:
        params = {
            "input": q2,
            "history": json.dumps(conversation)
        }
        
        response = requests.get(
            f"{BASE_URL}/api",
            params=params,
            headers=headers,
            timeout=30
        )
        
        assert response.status_code == 200, f"Q2: Expected 200, got {response.status_code}"
        data = response.json()
        answer2 = data.get('response', '')
        assert answer2, "Q2: No response received"
        
        print(f"✅ Response:\n{answer2}\n")
        
        conversation.append({"role": "user", "content": q2})
        conversation.append({"role": "assistant", "content": str(answer2)})
        
    except AssertionError as e:
        print(f"❌ Assertion Error: {e}\n")
        raise
    except Exception as e:
        print(f"❌ Error: {e}\n")
        raise
    
    print("="*60 + "\n")
    
    # Third question (continuing conversation)
    q3 = "What should I do when I fail at practicing this?"
    print(f"❓ Question 3: {q3}")
    print(f"📝 Conversation History: {len(conversation)} messages")
    print("-" * 60)
    
    try:
        params = {
            "input": q3,
            "history": json.dumps(conversation)
        }
        
        response = requests.get(
            f"{BASE_URL}/api",
            params=params,
            headers=headers,
            timeout=30
        )
        
        assert response.status_code == 200, f"Q3: Expected 200, got {response.status_code}"
        data = response.json()
        answer3 = data.get('response', '')
        assert answer3, "Q3: No response received"
        
        print(f"✅ Response:\n{answer3}\n")
        
        conversation.append({"role": "user", "content": q3})
        conversation.append({"role": "assistant", "content": str(answer3)})
        
    except AssertionError as e:
        print(f"❌ Assertion Error: {e}\n")
        raise
    except Exception as e:
        print(f"❌ Error: {e}\n")
        raise
    
    print("="*60)
    print(f"\n✅ Full Conversation History ({len(conversation)} messages):\n")
    for i, msg in enumerate(conversation, 1):
        print(f"{i}. {msg['role'].upper()}: {msg['content'][:80]}...")
        print()
    
    print("="*60)
    print("✅ Conversation History Test: All 3 questions passed\n")
    assert len(conversation) == 6, f"Expected 6 messages, got {len(conversation)}"


if __name__ == "__main__":
    print(f"🔑 API Token: {API_TOKEN}")
    print(f"🌐 Base URL: {BASE_URL}")
    
    test_basic_questions()
    test_conversation_history()
    
    print("✅ All tests complete!")