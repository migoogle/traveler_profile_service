import os
import json
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/reinject_traveler_profile', methods=['POST'])
def reinject_traveler_profile():
    """
    Handles the tool call from Agent Assist.
    1. Receives the JSON payload containing the tool arguments.
    2. Extracts the traveler profile data.
    3. Returns the structured 'agentDisplayMessage' for the UI.
    """
    try:
        # 1. Parse the Request
        # Agent Assist sends the tool parameters in the request body.
        request_data = request.get_json()
        
        app.logger.info(f"[APP] --- Received Request ---")
        app.logger.info(f"[APP] {json.dumps(request_data, indent=2)}")

        # The parameters might be directly in the root or nested under 'inputParameters'
        # depending on your OpenAPI/Connector setup. We handle both for robustness.
        parameters = request_data.get('inputParameters', request_data)

        # 2. Extract Data (and optionally validate/normalize)
        # We construct the response object using the input parameters.
        # This is where you could add logic like:
        # - Converting "next Tuesday" to "YYYY-MM-DD"
        # - Formatting currency strings
        # - Validating boolean flags
        
        agent_display_message = {
            # Basic Info
            "client_first_name": parameters.get("client_first_name"),
            "client_last_name": parameters.get("client_last_name"),
            "date_of_birth": parameters.get("date_of_birth"),
            "email_address": parameters.get("email_address"),
            "phone_number": parameters.get("phone_number"),
            
            # Trip Details
            "trip_start_date": parameters.get("trip_start_date"),
            "trip_end_date": parameters.get("trip_end_date"),
            "preferred_departure_details": parameters.get("preferred_departure_details"),
            "primary_stay_location": parameters.get("primary_stay_location"),
            "planned_booking_date": parameters.get("planned_booking_date"),
            
            # Preferences & Booleans (defaulting to None/Null if missing to avoid UI confusion)
            "has_booked_before": parameters.get("has_booked_before"),
            "has_loyalty_program": parameters.get("has_loyalty_program"),
            "is_primary_traveler": parameters.get("is_primary_traveler"),
            "has_valid_passport": parameters.get("has_valid_passport"),
            "interested_in_insurance": parameters.get("interested_in_insurance"),
            "winter_conditions_travel": parameters.get("winter_conditions_travel"),
            "is_business_purpose": parameters.get("is_business_purpose"),
            
            # Additional Context Fields
            "current_insurance_provider": parameters.get("current_insurance_provider"),
            "payment_preference": parameters.get("payment_preference"),
            "safety_tools_usage": parameters.get("safety_tools_usage"),
            "document_limitations": parameters.get("document_limitations"),
            
            # Catch-all for any other fields passed in the schema
            # This ensures forward compatibility if you add fields to the tool definition later.
            **{k: v for k, v in parameters.items() if k not in [
                "client_first_name", "client_last_name", "date_of_birth", 
                "email_address", "phone_number" 
                # ... add other explicitly mapped keys above to exclude them here if desired
            ]}
        }

        # Convert all values to strings, and null to " "
        for key, value in agent_display_message.items():
            if value is None:
                agent_display_message[key] = " "
            else:
                agent_display_message[key] = str(value)

        # 3. Construct Response
        # The structure matches the Output Schema defined in your tool:
        # { "agentDisplayMessage": { ... } }
        
        response_payload = {
            "agentDisplayMessage": agent_display_message
        }

        app.logger.info(f"[APP] --- Sending Response ---")
        app.logger.info(f"[APP] {json.dumps(response_payload, indent=2)}")

        return jsonify(response_payload), 200

    except Exception as e:
        app.logger.error(f"[APP] Error processing request: {e}")
        # Return a structured error so the UI handles it gracefully
        return jsonify({
            "error": str(e),
            "agentDisplayMessage": {"status": "error_processing_data"}
        }), 500

if __name__ == '__main__':
    # Cloud Run uses the PORT environment variable
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)