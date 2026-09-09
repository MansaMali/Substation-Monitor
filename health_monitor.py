def evaluate_transformer_health(
        temperature,
        load,
        average_voltage,
        increasing

):

        issues = []

        health_score = 100
        
        if temperature > 90:
    
            issues.append("Temperature dangerously high")

            health_score -= 40

        
        elif temperature > 80:
    
            issues.append("Temperature elevated") 
            health_score -= 20   
    
    
        if load > 90:
    
            issues.append("Load dangerously high") 
            health_score -= 30
    
        
        elif load > 80:
    
            issues.append("Load elevated")
            health_score -= 15

        if average_voltage < 7000:
    
            issues.append("Voltage below normal range")
            health_score -= 15
    
        if increasing >= 4:

            issues.append("Temperature consistently increasing")

            health_score -= 10

        if health_score < 0:
             
             health_score = 0

        if health_score >= 90:

             health_status = "NORMAL"

        elif health_score >= 70:
             
             health_status = "WATCH"

        elif  health_score >= 40:
             
             health_status = "WARNING"

        else:
            health_status = "CRITICAL"

        if issues:
                 
                 health_reason = "; ".join(issues)

        else:
                
                 health_reason = "Transformer operating normally"

        return health_status, health_reason, health_score