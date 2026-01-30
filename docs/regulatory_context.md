# EU MDR (Medical Device Regulation 2017/745) - Context for Our Project

## Overview

The EU Medical Device Regulation (MDR) 2017/745 establishes requirements for medical devices sold in the European Union. Software used for diagnosis, prediction, or treatment guidance is classified as a medical device.

## Classification

Our skin cancer detection system would likely be classified as:
- **Class IIa or IIb medical device** (depending on specific claims)
- Software intended for diagnosis of serious conditions

## Key Requirements Relevant to Our Project

### 1. General Safety and Performance Requirements (Annex I)

#### Risk Management (Article 3)
- Identify all known and foreseeable risks
- Minimize risks through design
- Provide information about residual risks to users

**Our Implementation:**
- Uncertainty quantification identifies high-risk predictions
- Deferral mechanism reduces risk of incorrect diagnoses
- Clear documentation of model limitations

#### Performance and Safety (Article 9)
- Device must perform as intended
- Benefits must outweigh risks
- Performance must be demonstrated through clinical evaluation

**Our Implementation:**
- Comprehensive evaluation metrics (AUROC, sensitivity, specificity)
- Calibration ensures accurate confidence scores
- Documentation of performance on diverse test sets

### 2. Software-Specific Requirements (Annex I, Chapter II, Section 17)

#### Software Validation
- Software development lifecycle must be appropriate
- Validation must demonstrate safety and performance
- Risk management throughout development

**Our Implementation:**
- Structured development process (Phase 0-6)
- Rigorous testing and validation
- Version control and documentation

#### Transparency and Explainability
- Users must understand how the software works
- Uncertainty and limitations must be communicated
- Results must be interpretable

**Our Implementation:**
- Uncertainty quantification (epistemic uncertainty)
- Calibrated confidence scores (users can trust probabilities)
- Deferral mechanism for unclear cases
- Clear visualization of predictions and uncertainty

#### Clinical Evidence
- Performance must be demonstrated in intended use population
- Clinical evaluation required
- Post-market surveillance needed

**Our Implementation:**
- Evaluation on diverse ISIC dataset
- Comprehensive performance metrics
- Documentation for future clinical validation

### 3. Technical Documentation Requirements (Annex II)

Must include:
- Device description and specifications
- Design and manufacturing information
- Risk management file
- Verification and validation results
- Instructions for use
- Clinical evaluation report

**Our Implementation:**
- Detailed README and documentation
- Phase reports documenting development
- Performance evaluation results
- Model cards with specifications
- Clear instructions for deployment

## Why Uncertainty Quantification Matters for EU MDR

### Transparency Requirement
EU MDR requires that medical devices be transparent about their limitations and uncertainty.

**Our Solution:**
- MC Dropout provides epistemic uncertainty
- Calibration ensures probabilities are trustworthy
- Uncertainty displayed to users

### Risk Management
Must identify and mitigate risks, especially false negatives (missing melanoma).

**Our Solution:**
- High uncertainty cases automatically flagged
- Deferral to dermatologist for uncertain cases
- Sensitivity can be tuned based on risk tolerance

### Clinical Usability
Clinicians must be able to understand and trust the system.

**Our Solution:**
- Calibrated probabilities (90% confidence means 90% correct)
- Confidence intervals show prediction uncertainty
- Clear visualization of decision-making

## Compliance Checklist for Our Project

### Pre-Development
- [x] Define intended use: Binary melanoma classification
- [x] Identify target population: Dermoscopic images
- [x] Establish risk management process
- [x] Plan evaluation strategy

### Development Phase
- [ ] Document dataset (ISIC 2018)
- [ ] Document model architecture (EfficientNet-B0)
- [ ] Document training process
- [ ] Implement uncertainty quantification
- [ ] Implement calibration
- [ ] Implement deferral mechanism

### Validation & Testing
- [ ] Evaluate on diverse test set
- [ ] Measure calibration quality (ECE)
- [ ] Analyze errors and edge cases
- [ ] Test deferral mechanism
- [ ] Document all results

### Documentation
- [ ] Create device description
- [ ] Document intended use and claims
- [ ] Risk management file
- [ ] Validation results
- [ ] Instructions for use
- [ ] Known limitations

### Post-Development (Beyond this project scope)
- [ ] Clinical validation study
- [ ] Regulatory submission preparation
- [ ] Post-market surveillance plan
- [ ] Incident reporting system

## Important Disclaimers

### For Our Portfolio Project

This project is **educational and demonstrative**. It is:
- ✓ Designed with EU MDR principles in mind
- ✓ Implements best practices for medical AI
- ✓ Demonstrates regulatory awareness

It is NOT:
- ✗ Intended for actual clinical use
- ✗ A complete regulatory submission
- ✗ Clinically validated
- ✗ CE marked

### For Real Deployment

A real medical device would require:
- Clinical validation studies
- Regulatory review and approval
- CE marking process
- Quality management system (ISO 13485)
- Post-market surveillance
- Incident reporting

## Key Principles for Medical AI

1. **Safety First**: Better to defer than to be confidently wrong
2. **Transparency**: Users must understand limitations
3. **Validation**: Performance must be rigorously tested
4. **Monitoring**: Track performance over time
5. **Documentation**: Everything must be documented

## References

- EU MDR 2017/745: https://eur-lex.europa.eu/eli/reg/2017/745/oj
- Medical Device Coordination Group (MDCG) guidance documents
- FDA guidance on Software as a Medical Device (SaMD)
- ISO 13485: Quality management for medical devices
- IEC 62304: Software lifecycle for medical device software

---

**Document Created**: 30/01/2026  
**Phase**: 0 - Foundation & Setup  
**Purpose**: Understand regulatory context for medical AI project